# Data Drift Detection in Machine Learning

## What is Data Drift?

**Data drift** occurs when the statistical properties of input data change over time
compared to the data used during model training.

Even if data passes validation checks, drift can still degrade model performance.

> Valid data can still be *wrong* for the model.

---

## Data Validation vs Data Drift (Important Difference)

| Aspect | Data Validation | Data Drift |
|------|----------------|-----------|
| Purpose | Check correctness | Monitor change |
| Question | “Is the data valid?” | “Is the data different?” |
| Action | Block pipeline | Trigger alerts / retraining |
| Timing | Before processing | During production |

Both are required in production ML systems.

---

## Why Data Drift Matters

Machine learning models learn patterns from historical data.
When input distributions change, those learned patterns may no longer apply.

Unmonitored drift can lead to:
- Gradual accuracy degradation
- Increased bias
- Silent model failure
- Poor business decisions

---

## Common Types of Drift

### 1. Feature Drift
Changes in input feature distributions.

Examples:
- Mean or variance shift
- Sudden spikes in values
- Category frequency changes

---

### 2. Label Drift
Changes in the target variable distribution (when labels are available).

Example:
- Fraud rate increases significantly over time

---

## Drift Detection Strategy Used in This Project

This project uses a **baseline-vs-current comparison** approach:

1. Training data is saved as a **baseline**
2. Incoming inference data is compared against the baseline
3. Statistical thresholds determine whether drift exists

Drift detection is **non-blocking** but **actionable**.

---

## Metrics Used for Drift Detection

For numeric features:
- Mean shift
- Standard deviation shift

Drift is flagged when relative change exceeds a threshold.

Example:
- Mean shift > 20%
- Standard deviation shift > 20%

---

## Example Drift Detection Logic (Conceptual)

```python
mean_shift = abs(new_mean - baseline_mean) / baseline_mean
std_shift = abs(new_std - baseline_std) / baseline_std
