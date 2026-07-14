from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from astropy.io import fits

from feature_extractor import find_observation_dirs


class PolixPolarimetryService:
    """
    Physical polarimetry diagnostic service for POLIX Level-2 observations.

    Outputs:
    - raw observed modulation
    - fitted modulation phase
    - blank-sky-relative Q/U modulation
    - PD sensitivity proxies under assumed mu100 values
    - fit quality and confidence status

    This service does NOT claim final calibrated PD or official sky PA.
    """

    def __init__(self, config_path):
        self.config_path = Path(config_path)

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Polarimetry configuration not found: {self.config_path}"
            )

        with self.config_path.open("r", encoding="utf-8") as file:
            self.config = json.load(file)

        vector_config = self.config["blank_sky_vector_baseline"]
        modulation_config = self.config["blank_sky_raw_modulation_baseline"]
        proxy_config = self.config["pd_proxy_settings"]
        threshold_config = self.config["confidence_thresholds"]

        self.blank_q_mean = float(vector_config["q_fraction_mean"])
        self.blank_u_mean = float(vector_config["u_fraction_mean"])
        self.blank_q_std = float(vector_config["q_fraction_std"])
        self.blank_u_std = float(vector_config["u_fraction_std"])

        self.blank_mod_mean_percent = float(
            modulation_config["mean_percent"]
        )
        self.blank_mod_std_percent = float(
            modulation_config["std_percent"]
        )

        self.mu100_scenarios = [
            float(value)
            for value in proxy_config["mu100_scenarios"]
        ]

        self.central_mu100 = float(
            proxy_config["central_mu100"]
        )

        self.moderate_threshold = float(
            threshold_config["moderate_vector_distance"]
        )
        self.strong_threshold = float(
            threshold_config["strong_vector_distance"]
        )

        self.scientific_warning = self.config[
            "scientific_limits"
        ]["required_warning"]

        self.angle_status = self.config[
            "angle_settings"
        ]["status"]

    # ------------------------------------------------------------------
    # File discovery
    # ------------------------------------------------------------------

    @staticmethod
    def _find_weightedroll_file(observation_dir):
        observation_dir = Path(observation_dir)

        polarization_dir = (
            observation_dir / "Polix_l2_polarization"
        )

        if not polarization_dir.exists():
            raise FileNotFoundError(
                f"Polix_l2_polarization directory not found in "
                f"{observation_dir}"
            )

        matches = sorted(
            polarization_dir.rglob("*WeightedRoll_L2.fits")
        )

        if not matches:
            raise FileNotFoundError(
                f"WeightedRoll_L2.fits not found in "
                f"{polarization_dir}"
            )

        return matches[0]

    # ------------------------------------------------------------------
    # FITS reading
    # ------------------------------------------------------------------

    @staticmethod
    def _find_column(column_names, exact_candidates, contains_candidates):
        name_map = {
            str(name).upper(): name
            for name in column_names
        }

        for candidate in exact_candidates:
            candidate_upper = candidate.upper()

            if candidate_upper in name_map:
                return name_map[candidate_upper]

        for original_name in column_names:
            upper_name = str(original_name).upper()

            if any(
                candidate.upper() in upper_name
                for candidate in contains_candidates
            ):
                return original_name

        return None

    def _read_weightedroll_curve(self, weightedroll_path):
        weightedroll_path = Path(weightedroll_path)

        with fits.open(
            weightedroll_path,
            memmap=True
        ) as hdul:

            table_data = None

            for hdu in hdul:
                if (
                    hdu.data is not None
                    and hasattr(hdu.data, "columns")
                ):
                    table_data = hdu.data
                    break

            if table_data is None:
                raise ValueError(
                    f"No FITS table found in {weightedroll_path}"
                )

            column_names = list(table_data.columns.names)

            angle_column = self._find_column(
                column_names,
                exact_candidates=[
                    "ROLL_AZ_ANG",
                    "ROLL_AZIMUTH_ANGLE",
                    "AZIMUTH_ANGLE",
                ],
                contains_candidates=[
                    "ROLL_AZ",
                    "AZIMUTH",
                ],
            )

            rate_column = self._find_column(
                column_names,
                exact_candidates=[
                    "TOTAL_COUNTRATE",
                    "TOTAL_COUNT_RATE",
                    "COUNTRATE",
                    "RATE",
                ],
                contains_candidates=[
                    "COUNTRATE",
                    "COUNT_RATE",
                ],
            )

            error_column = self._find_column(
                column_names,
                exact_candidates=[
                    "ERROR",
                    "ERR",
                    "RATE_ERROR",
                ],
                contains_candidates=[
                    "ERROR",
                    "ERR",
                ],
            )

            if angle_column is None:
                raise ValueError(
                    f"Angle column not found. Available columns: "
                    f"{column_names}"
                )

            if rate_column is None:
                raise ValueError(
                    f"Count-rate column not found. Available columns: "
                    f"{column_names}"
                )

            if error_column is None:
                raise ValueError(
                    f"Error column not found. Available columns: "
                    f"{column_names}"
                )

            angle_deg = np.asarray(
                table_data[angle_column],
                dtype=float
            ).reshape(-1)

            count_rate = np.asarray(
                table_data[rate_column],
                dtype=float
            ).reshape(-1)

            error = np.asarray(
                table_data[error_column],
                dtype=float
            ).reshape(-1)

        valid = (
            np.isfinite(angle_deg)
            & np.isfinite(count_rate)
            & np.isfinite(error)
            & (error > 0)
        )

        angle_deg = angle_deg[valid]
        count_rate = count_rate[valid]
        error = error[valid]

        if len(angle_deg) < 10:
            raise ValueError(
                f"Not enough valid WeightedRoll bins in "
                f"{weightedroll_path}"
            )

        return angle_deg, count_rate, error

    # ------------------------------------------------------------------
    # Modulation fitting
    # ------------------------------------------------------------------

    @staticmethod
    def _fit_modulation_curve(angle_deg, count_rate, error):
        phi = np.deg2rad(angle_deg)

        design_matrix = np.column_stack([
            np.ones_like(phi),
            np.cos(2.0 * phi),
            np.sin(2.0 * phi),
        ])

        weights = 1.0 / np.square(error)

        normal_matrix = (
            design_matrix.T
            @ (weights[:, None] * design_matrix)
        )

        right_side = (
            design_matrix.T
            @ (weights * count_rate)
        )

        covariance = np.linalg.pinv(normal_matrix)
        coefficients = covariance @ right_side

        c_level, q_coefficient, u_coefficient = coefficients

        fitted_rate = design_matrix @ coefficients
        residuals = count_rate - fitted_rate

        degrees_of_freedom = max(
            len(count_rate) - len(coefficients),
            1
        )

        chi_square = float(
            np.sum(np.square(residuals / error))
        )

        reduced_chi_square = (
            chi_square / degrees_of_freedom
        )

        amplitude = float(
            np.hypot(q_coefficient, u_coefficient)
        )

        if not np.isfinite(c_level) or c_level <= 0:
            raise ValueError(
                f"Invalid fitted mean level: {c_level}"
            )

        raw_modulation_fraction = amplitude / c_level
        raw_modulation_percent = (
            raw_modulation_fraction * 100.0
        )

        modulation_phase_deg = float(
            (
                0.5
                * np.rad2deg(
                    np.arctan2(
                        u_coefficient,
                        q_coefficient
                    )
                )
            )
            % 180.0
        )

        # --------------------------------------------------------------
        # Error propagation
        # --------------------------------------------------------------

        if amplitude > 0:
            amplitude_gradient = np.array([
                0.0,
                q_coefficient / amplitude,
                u_coefficient / amplitude,
            ])

            amplitude_variance = float(
                amplitude_gradient
                @ covariance
                @ amplitude_gradient
            )

            amplitude_error = float(
                np.sqrt(max(amplitude_variance, 0.0))
            )

            modulation_gradient = np.array([
                -amplitude / np.square(c_level),
                q_coefficient / (amplitude * c_level),
                u_coefficient / (amplitude * c_level),
            ])

            modulation_variance = float(
                modulation_gradient
                @ covariance
                @ modulation_gradient
            )

            raw_modulation_percent_error = float(
                np.sqrt(max(modulation_variance, 0.0))
                * 100.0
            )

            phase_gradient = np.array([
                0.0,
                -0.5
                * u_coefficient
                / np.square(amplitude),
                0.5
                * q_coefficient
                / np.square(amplitude),
            ])

            phase_variance_rad = float(
                phase_gradient
                @ covariance
                @ phase_gradient
            )

            modulation_phase_error_deg = float(
                np.rad2deg(
                    np.sqrt(max(phase_variance_rad, 0.0))
                )
            )

        else:
            amplitude_error = np.nan
            raw_modulation_percent_error = np.nan
            modulation_phase_error_deg = np.nan

        amplitude_snr = (
            amplitude / amplitude_error
            if (
                np.isfinite(amplitude_error)
                and amplitude_error > 0
            )
            else np.nan
        )

        if reduced_chi_square <= 2.0:
            fit_quality = "acceptable"
        elif reduced_chi_square <= 5.0:
            fit_quality = "caution"
        else:
            fit_quality = "poor_simple_sinusoid_fit"

        return {
            "C_mean_level": float(c_level),
            "Q_cos2_coeff": float(q_coefficient),
            "U_sin2_coeff": float(u_coefficient),

            "raw_modulation_fraction": float(
                raw_modulation_fraction
            ),
            "raw_modulation_percent": float(
                raw_modulation_percent
            ),
            "raw_modulation_percent_error": float(
                raw_modulation_percent_error
            ),

            "modulation_phase_deg": float(
                modulation_phase_deg
            ),
            "modulation_phase_error_deg": float(
                modulation_phase_error_deg
            ),

            "amplitude_snr": float(amplitude_snr),
            "chi_square": float(chi_square),
            "reduced_chi2": float(
                reduced_chi_square
            ),
            "fit_quality": fit_quality,
        }

    # ------------------------------------------------------------------
    # Blank-sky-relative analysis
    # ------------------------------------------------------------------

    def _add_background_relative_results(self, result):
        c_level = result["C_mean_level"]
        q_coefficient = result["Q_cos2_coeff"]
        u_coefficient = result["U_sin2_coeff"]

        q_fraction = q_coefficient / c_level
        u_fraction = u_coefficient / c_level

        q_minus_blank = (
            q_fraction - self.blank_q_mean
        )

        u_minus_blank = (
            u_fraction - self.blank_u_mean
        )

        relative_modulation_fraction = float(
            np.hypot(
                q_minus_blank,
                u_minus_blank
            )
        )

        relative_modulation_percent = (
            relative_modulation_fraction * 100.0
        )

        relative_phase_deg = float(
            (
                0.5
                * np.rad2deg(
                    np.arctan2(
                        u_minus_blank,
                        q_minus_blank
                    )
                )
            )
            % 180.0
        )

        q_blank_z = (
            q_minus_blank / self.blank_q_std
            if self.blank_q_std > 0
            else np.nan
        )

        u_blank_z = (
            u_minus_blank / self.blank_u_std
            if self.blank_u_std > 0
            else np.nan
        )

        vector_distance = float(
            np.hypot(q_blank_z, u_blank_z)
        )

        if vector_distance >= self.strong_threshold:
            vector_status = (
                "strong_background_relative_vector_difference"
            )
        elif vector_distance >= self.moderate_threshold:
            vector_status = (
                "moderate_background_relative_vector_difference"
            )
        else:
            vector_status = (
                "within_blank_sky_vector_scatter"
            )

        raw_modulation_z = (
            (
                result["raw_modulation_percent"]
                - self.blank_mod_mean_percent
            )
            / self.blank_mod_std_percent
            if self.blank_mod_std_percent > 0
            else np.nan
        )

        if raw_modulation_z >= 2.0:
            raw_modulation_status = (
                "above_blank_sky_baseline"
            )
        elif raw_modulation_z <= -2.0:
            raw_modulation_status = (
                "below_blank_sky_baseline"
            )
        else:
            raw_modulation_status = (
                "within_blank_sky_baseline_range"
            )

        result.update({
            "q_fraction": float(q_fraction),
            "u_fraction": float(u_fraction),
            "q_percent": float(q_fraction * 100.0),
            "u_percent": float(u_fraction * 100.0),

            "background_relative_modulation_fraction": float(
                relative_modulation_fraction
            ),
            "background_relative_modulation_percent": float(
                relative_modulation_percent
            ),
            "background_relative_phase_deg": float(
                relative_phase_deg
            ),
            "background_relative_vector_distance": float(
                vector_distance
            ),
            "background_relative_vector_status": (
                vector_status
            ),

            "source_vs_blank_z": float(
                raw_modulation_z
            ),
            "source_modulation_vs_blank_status": (
                raw_modulation_status
            ),
        })

        return result

    # ------------------------------------------------------------------
    # PD proxy sensitivity values
    # ------------------------------------------------------------------

    def _add_pd_proxy_results(self, result):
        raw_modulation_percent = (
            result["raw_modulation_percent"]
        )

        relative_modulation_percent = result[
            "background_relative_modulation_percent"
        ]

        pd_sensitivity = {}

        for mu100 in self.mu100_scenarios:
            label = f"mu{int(round(mu100 * 100))}"

            pd_sensitivity[label] = {
                "assumed_mu100": float(mu100),
                "raw_pd_proxy_percent": float(
                    raw_modulation_percent / mu100
                ),
                "background_relative_pd_proxy_percent": float(
                    relative_modulation_percent / mu100
                ),
            }

        result["pd_proxy_sensitivity"] = pd_sensitivity

        result["selected_proxy_mu100"] = float(
            self.central_mu100
        )

        result["selected_raw_pd_proxy_percent"] = float(
            raw_modulation_percent / self.central_mu100
        )

        result[
            "selected_background_relative_pd_proxy_percent"
        ] = float(
            relative_modulation_percent
            / self.central_mu100
        )

        result["reported_angle_value_deg"] = float(
            result["modulation_phase_deg"]
        )

        result["reported_angle_type"] = (
            "fitted_modulation_phase_not_official_PA"
        )

        result["pa_conversion_status"] = (
            self.angle_status
        )

        result["scientific_warning"] = (
            self.scientific_warning
        )

        return result

    # ------------------------------------------------------------------
    # Confidence interpretation
    # ------------------------------------------------------------------

    @staticmethod
    def _add_confidence_status(result):
        fit_quality = result["fit_quality"]

        vector_status = result[
            "background_relative_vector_status"
        ]

        if (
            vector_status
            == "strong_background_relative_vector_difference"
            and fit_quality == "acceptable"
        ):
            confidence_status = (
                "strong_proxy_candidate_calibration_required"
            )

        elif (
            vector_status
            == "moderate_background_relative_vector_difference"
            and fit_quality == "acceptable"
        ):
            confidence_status = (
                "moderate_proxy_candidate_calibration_required"
            )

        elif (
            vector_status
            in {
                "moderate_background_relative_vector_difference",
                "strong_background_relative_vector_difference",
            }
            and fit_quality != "acceptable"
        ):
            confidence_status = (
                "low_confidence_due_to_fit_quality"
            )

        else:
            confidence_status = (
                "within_blank_sky_scatter_not_detection"
            )

        result["polarimetry_confidence_status"] = (
            confidence_status
        )

        result["final_calibrated_pd_claimed"] = False
        result["official_pa_claimed"] = False

        return result

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def analyze_observation_dir(self, observation_dir):
        observation_dir = Path(observation_dir)

        weightedroll_path = (
            self._find_weightedroll_file(
                observation_dir
            )
        )

        angle_deg, count_rate, error = (
            self._read_weightedroll_curve(
                weightedroll_path
            )
        )

        result = self._fit_modulation_curve(
            angle_deg,
            count_rate,
            error
        )

        observation_id = observation_dir.name.replace(
            "_L2_V1p1",
            ""
        )

        result.update({
            "observation_id": observation_id,
            "weightedroll_filename": (
                weightedroll_path.name
            ),
            "weightedroll_bins_used": int(
                len(angle_deg)
            ),
        })

        result = self._add_background_relative_results(
            result
        )

        result = self._add_pd_proxy_results(
            result
        )

        result = self._add_confidence_status(
            result
        )

        return result

    def analyze_extracted_root(self, extracted_root):
        extracted_root = Path(extracted_root)

        observation_dirs = find_observation_dirs(
            extracted_root
        )

        if not observation_dirs:
            raise ValueError(
                "No valid POLIX Level-2 observation folders "
                "were found for polarimetry analysis."
            )

        results = []

        for observation_dir in observation_dirs:
            try:
                result = self.analyze_observation_dir(
                    observation_dir
                )
                results.append(result)

            except Exception as exc:
                results.append({
                    "observation_id": (
                        observation_dir.name.replace(
                            "_L2_V1p1",
                            ""
                        )
                    ),
                    "polarimetry_error": str(exc),
                    "final_calibrated_pd_claimed": False,
                    "official_pa_claimed": False,
                })

        return results