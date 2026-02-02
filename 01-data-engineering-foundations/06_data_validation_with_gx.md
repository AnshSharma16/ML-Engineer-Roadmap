# Data Validation with Great Expectations (GX)

## Why Great Expectations?

**Great Expectations (GX)** is a data quality and validation framework used in
production ML and data engineering pipelines to ensure that data is **correct,
consistent, and reliable** before it is consumed by models.

GX is commonly used in:
- Batch data pipelines (Airflow, Spark)
- Feature engineering pipelines
- Training and inference validation gates
- CI/CD data quality checks

---

## What Problem GX Solves

Machine learning systems fail silently when data quality degrades.
Great Expectations prevents this by enforcing **explicit rules** on data.

Examples of real-world failures GX prevents:
- Null or duplicate IDs
- Negative prices or quantities
- Unexpected categorical values
- Schema changes in upstream data sources

> Bad data should stop the pipeline — not the model.

---

## Core GX Concepts (Must Know)

### 1. Data Asset
A **Data Asset** represents a dataset to be validated.
Examples:
- CSV file
- Database table
- Pandas DataFrame
- Spark DataFrame

---

### 2. Expectation
An **Expectation** is a rule about the data.

Examples:
- Column must not be null
- Values must be within a range
- Column must be unique
- Column values must belong to a set

---

### 3. Expectation Suite
A collection of expectations applied together.
It defines **what “good data” means**.

---

### 4. Validation Result
The output of running expectations against data.
- Pass / Fail
- Row-level failure details
- Summary statistics

---

## Example Expectations (Conceptual)

```python
ExpectColumnValuesToNotBeNull(column="order_id")
ExpectColumnValuesToBeUnique(column="order_id")
ExpectColumnValuesToBeBetween(column="price", min_value=0)
ExpectColumnValuesToBeInSet(
    column="sales_channel",
    value_set=["Online", "Offline"]
)
