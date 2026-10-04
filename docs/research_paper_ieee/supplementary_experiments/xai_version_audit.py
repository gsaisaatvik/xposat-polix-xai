"""Audit Sco X-1 with the exact XAI implementation imported from model_service.py.

This script intentionally does not reimplement the XAI formula.  It imports
PolixXAIPredictor, executes predict_dataframe/explain_one, and uses a Python
trace hook only to retain the complete 15-row local `rows` list that
explain_one sorts before returning its top five rows.
"""

from __future__ import annotations

import hashlib
import inspect
import json
import subprocess
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(r"D:\polix_xai_webapp")
PAPER_ROOT = PROJECT_ROOT / "research_paper_ieee"
SUPPLEMENTARY = PAPER_ROOT / "supplementary_experiments"
MODEL_SERVICE_PATH = PROJECT_ROOT / "model_service.py"
MODEL_PATH = (
    PROJECT_ROOT / "model" / "polix_v2_matrixC_unsupervised_xai_model.pkl"
)
MATRIX_PATH = Path(
    r"D:\ISROtrial\Polix_L2_full_archive\final_project_outputs"
    r"\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv"
)
NOTEBOOK_ALL_XAI_PATH = Path(
    r"D:\ISROtrial\Polix_L2_full_archive"
    r"\v2_unsupervised_xai_all_feature_contributions.csv"
)
PRIOR_REPRODUCTION_PATH = (
    SUPPLEMENTARY / "deployed_xai_reproduction.csv"
)
OUTPUT_PATH = (
    SUPPLEMENTARY / "deployed_xai_exact_from_model_service.csv"
)
METADATA_PATH = SUPPLEMENTARY / "xai_version_audit_metadata.json"
OBSERVATION_ID = "X01_PLX_G01_0006_000000"
MATRIX_NAME = "C_primary_plus_supporting"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args],
        cwd=PROJECT_ROOT,
        text=True,
        encoding="utf-8",
    ).strip()


def main() -> None:
    sys.path.insert(0, str(PROJECT_ROOT))
    import model_service  # noqa: PLC0415

    predictor = model_service.PolixXAIPredictor(str(MODEL_PATH))
    matrix = pd.read_csv(MATRIX_PATH)
    selected = matrix.loc[
        matrix["observation_id"].eq(OBSERVATION_ID)
    ].copy()
    if len(selected) != 1:
        raise RuntimeError(
            f"Expected one {OBSERVATION_ID} row; found {len(selected)}"
        )

    # Execute the same public method used by the Flask application.
    prediction = predictor.predict_dataframe(selected)[0]

    # Execute the exact deployed explain_one function again.  The trace hook
    # captures its already-computed and already-sorted 15-row local variable
    # before the function returns only rows[:5].
    scaled = predictor.scaler.transform(
        selected[predictor.feature_cols]
    )[0]
    captured: dict[str, object] = {}
    explain_code = predictor.explain_one.__func__.__code__

    def trace(frame, event, arg):
        if (
            event == "return"
            and frame.f_code is explain_code
            and "rows" in frame.f_locals
        ):
            captured["rows"] = [
                dict(row) for row in frame.f_locals["rows"]
            ]
        return trace

    sys.settrace(trace)
    try:
        direct_top_five = predictor.explain_one(scaled)
    finally:
        sys.settrace(None)

    all_rows = captured.get("rows")
    if not isinstance(all_rows, list) or len(all_rows) != 15:
        raise RuntimeError(
            "Trace hook did not capture the 15 sorted rows from explain_one"
        )
    if direct_top_five != all_rows[:5]:
        raise RuntimeError("Captured rows do not match explain_one return")
    if prediction["top_xai_features"] != direct_top_five:
        raise RuntimeError(
            "predict_dataframe and direct explain_one outputs differ"
        )

    exact = pd.DataFrame(all_rows)
    exact.insert(0, "exact_rank", range(1, len(exact) + 1))
    exact.insert(0, "observation_id", OBSERVATION_ID)
    exact["exact_function_source"] = (
        r"D:\polix_xai_webapp\model_service.py::"
        "PolixXAIPredictor.explain_one"
    )

    prior = pd.read_csv(PRIOR_REPRODUCTION_PATH)
    prior = prior.loc[
        prior["observation_id"].eq(OBSERVATION_ID),
        ["feature", "rank", "combined_xai_score"],
    ].rename(
        columns={
            "rank": "prior_reproduction_rank",
            "combined_xai_score": "prior_reproduction_score",
        }
    )

    notebook = pd.read_csv(NOTEBOOK_ALL_XAI_PATH)
    notebook = notebook.loc[
        notebook["observation_id"].eq(OBSERVATION_ID)
        & notebook["matrix"].eq(MATRIX_NAME),
        ["feature", "combined_xai_score"],
    ].copy()
    notebook["notebook10_rank"] = notebook[
        "combined_xai_score"
    ].rank(method="first", ascending=False).astype(int)
    notebook = notebook.rename(
        columns={"combined_xai_score": "notebook10_score"}
    )

    exact = exact.merge(prior, on="feature", how="left")
    exact = exact.merge(notebook, on="feature", how="left")
    exact["delta_vs_prior_reproduction"] = (
        exact["xai_score"] - exact["prior_reproduction_score"]
    )
    exact["delta_vs_notebook10"] = (
        exact["xai_score"] - exact["notebook10_score"]
    )
    exact.to_csv(OUTPUT_PATH, index=False)

    metadata = {
        "observation_id": OBSERVATION_ID,
        "git_commit": git_output("rev-parse", "HEAD"),
        "git_model_service_diff": git_output(
            "diff", "--", "model_service.py"
        ),
        "model_service_sha256": sha256(MODEL_SERVICE_PATH),
        "model_pkl_sha256": sha256(MODEL_PATH),
        "matrix_c_sha256": sha256(MATRIX_PATH),
        "notebook10_all_xai_sha256": sha256(
            NOTEBOOK_ALL_XAI_PATH
        ),
        "prior_reproduction_sha256": sha256(
            PRIOR_REPRODUCTION_PATH
        ),
        "normalization_function_source": inspect.getsource(
            model_service.normalize_score
        ),
        "explain_one_source": inspect.getsource(
            model_service.PolixXAIPredictor.explain_one
        ),
        "prediction": prediction["prediction"],
        "anomaly_score": prediction["anomaly_score"],
        "top_five": direct_top_five,
        "max_absolute_delta_vs_prior_reproduction": float(
            exact["delta_vs_prior_reproduction"].abs().max()
        ),
        "max_absolute_delta_vs_notebook10": float(
            exact["delta_vs_notebook10"].abs().max()
        ),
        "python": sys.version,
        "pandas": pd.__version__,
    }
    METADATA_PATH.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    print(exact.to_string(index=False))
    print(f"\nWrote: {OUTPUT_PATH}")
    print(f"Wrote: {METADATA_PATH}")


if __name__ == "__main__":
    main()
