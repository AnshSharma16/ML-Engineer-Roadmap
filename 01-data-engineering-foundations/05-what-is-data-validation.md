# Data Validation in Machine Learning

## What is Data Validation?

**Data validation in machine learning** is the process of ensuring that data used for training and inference is **correct, consistent, complete, and reliable**.

It acts as a **quality gate** before data enters an ML pipeline. Even the best model will fail if trained on bad or inconsistent data.

> Garbage in → Garbage out (GIGO)

---

## Why Data Validation Matters

In real-world ML systems:
- Data comes from multiple sources (APIs, databases, logs)
- Data formats and distributions change over time
- Errors often go unnoticed but silently degrade model performance

Data validation helps to:
- Prevent training on corrupted or invalid data
- Catch errors early in the pipeline
- Ensure training and inference data are consistent
- Build **production-ready ML systems**

---

## What Do We Validate?

### 1. Schema Validation
Ensures the structure of data is correct.
- Expected columns exist
- No extra or missing columns
- Correct data types

Example:
- `age` → integer
- `salary` → float
- `gender` → categorical

---

### 2. Missing Values
Checks for null or missing values.
- Are missing values allowed?
- Are they within acceptable limits?

Example:
- ❌ 30% missing values in a critical column
- ✅ <5% missing values (can be imputed)

---

### 3. Range and Constraint Checks
Ensures values fall within valid bounds.

Examples:
- Age must be between 0 and 120
- Probability values must be between 0 and 1
- Ratings must be between 1 and 5

---

### 4. Statistical Validation
Compares distributions across datasets.
- Training vs validation
- Training vs production

Common checks:
- Mean and standard deviation
- Min and max values
- Percentiles

Used to detect **data drift**.

---

### 5. Uniqueness and Duplicates
- Primary keys should be unique
- Duplicate rows can bias training data

---

### 6. Label Validation (Supervised Learning)
- Labels must exist
- No invalid classes
- Class imbalance should be monitored

---

## Data Validation in the ML Lifecycle

| Stage | Validation Focus |
|------|------------------|
| Data Ingestion | Schema, types, nulls |
| Training | Distributions, labels |
| Evaluation | Train-test leakage |
| Inference | Schema consistency |
| Monitoring | Drift and anomalies |

---

## Common Tools for Data Validation

- **Great Expectations**
- **Pandera**
- **TensorFlow Data Validation (TFDV)**
- Custom Python assertions

Start simple. Many production systems rely on basic checks.

---

## Simple Python Example

```python
assert df["age"].between(0, 120).all()
assert df["salary"].isnull().mean() < 0.05
