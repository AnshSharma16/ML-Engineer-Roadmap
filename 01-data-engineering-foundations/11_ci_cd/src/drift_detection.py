import pandas as pd

def detect_drift(baseline_df, new_df, column, threshold=0.2):
    baseline_mean = baseline_df[column].mean()
    new_mean = new_df[column].mean()

    shift = abs(new_mean - baseline_mean) / baseline_mean

    return {
        "column": column,
        "baseline_mean": baseline_mean,
        "new_mean": new_mean,
        "mean_shift": shift,
        "drift_detected": shift > threshold
    }
