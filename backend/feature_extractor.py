import tarfile
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from astropy.io import fits


MATRIX_C_COLUMNS = [
    "observation_id",
    "t1A_exp_uniformity_cv",
    "t1A_exp_max_to_min_roll",
    "t1A_energy_peak_channel",
    "t1A_energy_weighted_mean_channel",
    "t1A_energy_weighted_std_channel",
    "t1A_energy_high_channel_fraction",
    "t1A_energy_channel_entropy",
    "t1A_energy_anode_balance_cv",
    "t1B_src_peak_to_median_roll",
    "t1B_src_roll_entropy",
    "t1B_src_roll_smoothness_norm",
    "t2_lc_rate_cv",
    "t2_lc_peak_to_median_rate",
    "t2_det_lc_rate_balance_cv",
    "t2_det_pha_centroid_spread",
]


def safe_div(a, b):
    if b is None or b == 0 or not np.isfinite(b):
        return np.nan
    return float(a / b)


def entropy_from_values(values):
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    values = values[values > 0]

    if values.size == 0:
        return np.nan

    p = values / values.sum()
    return float(-(p * np.log2(p)).sum())


def smoothness(values):
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]

    if values.size < 2:
        return np.nan

    return float(np.mean(np.abs(np.diff(values))))


def weighted_mean_std(channels, counts):
    counts = np.asarray(counts, dtype=float)
    channels = np.asarray(channels, dtype=float)

    total = counts.sum()

    if total <= 0:
        return np.nan, np.nan

    mean = float((channels * counts).sum() / total)
    var = float(((channels - mean) ** 2 * counts).sum() / total)

    return mean, np.sqrt(var)


def extract_archive(upload_path, output_dir):
    upload_path = Path(upload_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if upload_path.suffix == ".zip":
        with zipfile.ZipFile(upload_path, "r") as z:
            z.extractall(output_dir)

    elif upload_path.name.endswith(".tgz") or upload_path.name.endswith(".tar.gz"):
        with tarfile.open(upload_path, "r:gz") as t:
            t.extractall(output_dir)

    else:
        raise ValueError("Unsupported compressed file. Upload .zip, .tgz, or .tar.gz")

    return output_dir


def find_observation_dirs(root):
    root = Path(root)
    obs_dirs = []

    for p in root.rglob("*"):
        if not p.is_dir():
            continue

        if (p / "Polix_l2_lcpha").exists() and (p / "Polix_l2_polarization").exists():
            obs_dirs.append(p)

    return sorted(obs_dirs)


def find_file(folder, pattern, exclude_contains=None):
    """
    Find a file recursively.

    POLIX files usually include an observation-ID prefix, for example:
    X01_PLX_P01_0005_000000_Exp_Azimuth_Roll_L2.fits

    Therefore, if an exact filename is not found, search by filename suffix.
    """
    folder = Path(folder)

    # First try the supplied pattern directly
    files = list(folder.rglob(pattern))

    # If pattern has no wildcard and exact lookup failed,
    # allow an observation-ID prefix.
    if not files and not any(char in pattern for char in "*?[]"):
        files = list(folder.rglob(f"*{pattern}"))

    if exclude_contains:
        excluded_text = exclude_contains.lower()
        files = [
            file
            for file in files
            if excluded_text not in file.name.lower()
        ]

    files = sorted(files, key=lambda file: str(file).lower())

    if not files:
        return None

    return files[0]


def read_first_data_hdu(path):
    with fits.open(path, memmap=True) as hdul:
        for hdu in hdul:
            if hdu.data is not None:
                return np.asarray(hdu.data)
    raise ValueError(f"No data found in FITS file: {path}")


def extract_matrix_c_features(obs_dir):
    obs_dir = Path(obs_dir)

    pol = obs_dir / "Polix_l2_polarization"
    lcpha = obs_dir / "Polix_l2_lcpha"

    row = {}
    row["observation_id"] = obs_dir.name.replace("_L2_V1p1", "")

    # ------------------------------------------------------------------
    # Tier 1A Exposure features
    # ------------------------------------------------------------------
    exp_file = find_file(pol, "Exp_Azimuth_Roll_L2.fits")

    if exp_file is None:
        raise FileNotFoundError("Exp_Azimuth_Roll_L2.fits not found")

    with fits.open(exp_file) as hdul:
        data = hdul[1].data

        exposure_cols = [
            c for c in data.columns.names
            if "Exposure" in c or "EXPOSURE" in c
        ]

        exposures = np.vstack([np.asarray(data[c], dtype=float) for c in exposure_cols]).T
        roll_total_exp = np.nansum(exposures, axis=1)

    mean_exp = np.nanmean(roll_total_exp)
    std_exp = np.nanstd(roll_total_exp)

    row["t1A_exp_uniformity_cv"] = safe_div(std_exp, mean_exp)
    row["t1A_exp_max_to_min_roll"] = safe_div(np.nanmax(roll_total_exp), np.nanmin(roll_total_exp))

    # ------------------------------------------------------------------
    # Tier 1A EnergyRes features
    # ------------------------------------------------------------------
    energy_file = find_file(pol, "EnergyRes_Src_Azimuth_Roll_L2.fits")

    if energy_file is None:
        raise FileNotFoundError("EnergyRes_Src_Azimuth_Roll_L2.fits not found")

    energy = read_first_data_hdu(energy_file).astype(float)

    # Channel axis is usually 8192, largest dimension
    channel_axis = int(np.argmax(energy.shape))
    channel_count = energy.shape[channel_axis]

    spectrum = np.nansum(energy, axis=tuple(i for i in range(energy.ndim) if i != channel_axis))
    channels = np.arange(channel_count)

    total_counts = np.nansum(spectrum)

    row["t1A_energy_peak_channel"] = int(np.nanargmax(spectrum))
    row["t1A_energy_weighted_mean_channel"], row["t1A_energy_weighted_std_channel"] = weighted_mean_std(
        channels,
        spectrum
    )

    high_mask = channels >= 4000
    row["t1A_energy_high_channel_fraction"] = safe_div(np.nansum(spectrum[high_mask]), total_counts)
    row["t1A_energy_channel_entropy"] = entropy_from_values(spectrum)

    # anode axis usually has size 48
    anode_axis_candidates = [i for i, s in enumerate(energy.shape) if s == 48]

    if anode_axis_candidates:
        anode_axis = anode_axis_candidates[0]
        anode_counts = np.nansum(energy, axis=tuple(i for i in range(energy.ndim) if i != anode_axis))
        row["t1A_energy_anode_balance_cv"] = safe_div(np.nanstd(anode_counts), np.nanmean(anode_counts))
    else:
        row["t1A_energy_anode_balance_cv"] = np.nan

    # ------------------------------------------------------------------
    # Tier 1B Source Azimuth diagnostic features
    # ------------------------------------------------------------------
    src_file = find_file(pol, "Src_Azimuth_Roll_L2.fits", exclude_contains="EnergyRes")

    if src_file is None:
        raise FileNotFoundError("Src_Azimuth_Roll_L2.fits not found")

    with fits.open(src_file) as hdul:
        data = hdul[1].data
        anode_counts = np.asarray(data["ANODE_COUNTS"], dtype=float)
        roll_counts = np.nansum(anode_counts, axis=1)

    mean_roll_counts = np.nanmean(roll_counts)

    row["t1B_src_peak_to_median_roll"] = safe_div(np.nanmax(roll_counts), np.nanmedian(roll_counts))
    row["t1B_src_roll_entropy"] = entropy_from_values(roll_counts)
    row["t1B_src_roll_smoothness_norm"] = safe_div(smoothness(roll_counts), mean_roll_counts)

    # ------------------------------------------------------------------
    # Tier 2 Light curve features
    # ------------------------------------------------------------------
    lc_file = find_file(lcpha, "EventdataSource_L2.lc")

    if lc_file is None:
        raise FileNotFoundError("EventdataSource_L2.lc not found")

    with fits.open(lc_file) as hdul:
        data = hdul[1].data
        rates = np.asarray(data["RATE"], dtype=float)

    row["t2_lc_rate_cv"] = safe_div(np.nanstd(rates), np.nanmean(rates))
    row["t2_lc_peak_to_median_rate"] = safe_div(np.nanmax(rates), np.nanmedian(rates))

    # ------------------------------------------------------------------
    # Tier 2 Detector balance features
    # ------------------------------------------------------------------
    det_lc_means = []
    det_centroids = []

    for det in [1, 2, 3, 4]:
        det_lc = find_file(pol, f"ProcessedEventdataSource_Det{det}_L2.lc")
        det_pha = find_file(pol, f"ProcessedEventdataSource_Det{det}_L2.pha")

        if det_lc is not None:
            with fits.open(det_lc) as hdul:
                rates = np.asarray(hdul[1].data["RATE"], dtype=float)
                det_lc_means.append(np.nanmean(rates))

        if det_pha is not None:
            with fits.open(det_pha) as hdul:
                pha = hdul[1].data
                channels = np.asarray(pha["CHANNEL"], dtype=float)
                counts = np.asarray(pha["COUNTS"], dtype=float)
                centroid, _ = weighted_mean_std(channels, counts)
                det_centroids.append(centroid)

    row["t2_det_lc_rate_balance_cv"] = safe_div(np.nanstd(det_lc_means), np.nanmean(det_lc_means))
    row["t2_det_pha_centroid_spread"] = float(np.nanstd(det_centroids)) if det_centroids else np.nan

    return row


def extract_matrix_c_from_uploaded_archive(upload_path, temp_dir):
    extracted_dir = extract_archive(upload_path, temp_dir)
    obs_dirs = find_observation_dirs(extracted_dir)

    if not obs_dirs:
        raise ValueError(
            "No valid POLIX Level-2 observation folder found. "
            "Expected Polix_l2_lcpha/ and Polix_l2_polarization/ inside upload."
        )

    rows = []

    for obs_dir in obs_dirs:
        rows.append(extract_matrix_c_features(obs_dir))

    df = pd.DataFrame(rows)

    return df[MATRIX_C_COLUMNS]