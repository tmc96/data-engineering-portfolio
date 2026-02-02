import os

import pandas as pd
from alerts.alert_logic import trigger_alert
# -----------------------------
# CONFIG
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "bank_transactions_data_2.csv")

CRITICAL_COLUMNS = [
    "TransactionID",
    "TransactionDate",
    "TransactionAmount"
]

EXPECTED_SCHEMA = {
    "TransactionID": "Int64",
    "TransactionDate": "object",  # often string before parsing
    "TransactionAmount": "float64"
}

VOLUME_SPIKE_THRESHOLD_UPPER = 2.0
VOLUME_SPIKE_THRESHOLD_LOWER = 0.5


# -----------------------------
# LOAD DATA
# -----------------------------
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    df["TransactionID"] = pd.to_numeric(
        df["TransactionID"], errors="coerce"
    ).astype("Int64")   # <- NOTE capital I
    
    return df


# -----------------------------
# CHECK 1: MISSING VALUES
# -----------------------------
def check_missing_values(df: pd.DataFrame):
    missing = df[CRITICAL_COLUMNS].isnull().sum()
    missing = missing[missing > 0]

    if not missing.empty:
        trigger_alert(
            "Missing Values Detected",
            missing.to_dict()
        )


# -----------------------------
# CHECK 2: SCHEMA VALIDATION
# -----------------------------
def check_schema(df: pd.DataFrame):
    issues = {}

    # Missing columns
    missing_cols = set(EXPECTED_SCHEMA.keys()) - set(df.columns)
    if missing_cols:
        issues["missing_columns"] = list(missing_cols)

    # Data type mismatches
    dtype_issues = {}
    for col, expected_dtype in EXPECTED_SCHEMA.items():
        if col in df.columns:
            actual_dtype = str(df[col].dtype)
            if actual_dtype != expected_dtype:
                dtype_issues[col] = {
                    "expected": expected_dtype,
                    "actual": actual_dtype
                }

    if dtype_issues:
        issues["datatype_mismatches"] = dtype_issues

    if issues:
        trigger_alert("Schema Validation Failed", issues)


# -----------------------------
# CHECK 3: DATA VOLUME SPIKE
# -----------------------------
def check_data_volume(df: pd.DataFrame):
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"], errors="coerce")

    daily_counts = df.groupby(df["TransactionDate"].dt.date).size()

    avg_volume = daily_counts.mean()
    latest_day = daily_counts.index.max()
    latest_count = daily_counts.loc[latest_day]

    if latest_count > avg_volume * VOLUME_SPIKE_THRESHOLD_UPPER:
        trigger_alert(
            "Data Volume Spike Detected",
            {
                "date": str(latest_day),
                "count": int(latest_count),
                "average": float(avg_volume)
            }
        )

    if latest_count < avg_volume * VOLUME_SPIKE_THRESHOLD_LOWER:
        trigger_alert(
            "Data Volume Drop Detected",
            {
                "date": str(latest_day),
                "count": int(latest_count),
                "average": float(avg_volume)
            }
        )


# -----------------------------
# MAIN
# -----------------------------
def main():
    df = load_data(DATA_PATH)

    check_missing_values(df)
    check_schema(df)
    check_data_volume(df)

    print("Data quality checks completed.")


if __name__ == "__main__":
    main()