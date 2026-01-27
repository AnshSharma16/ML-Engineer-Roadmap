# 1.2 ETL vs ELT (Very Important)

## ETL: Extract → Transform → Load
Data is extracted from sources, transformed in a separate processing system, and then loaded into a data warehouse.

**Characteristics:**
- Transform before storage
- Rigid schema
- Slower to adapt to new ML features
- Common in traditional BI systems

**Example:**  
Clean CSV files → aggregate → load into warehouse

---

## ELT: Extract → Load → Transform
Data is extracted and loaded **raw** into a data warehouse or data lake, then transformed using scalable compute.

**Characteristics:**
- Store raw data first
- Flexible schema
- Supports large-scale ML feature creation
- Leverages modern cloud warehouses

**Example:**  
Load raw logs → create features later for training/inference

---

## Why ML Prefers ELT
- ML requires **raw historical data**
- Features evolve over time
- Multiple models may need different transformations
- Enables reproducibility and experimentation
- Avoids losing information early

> ML pipelines optimize for **flexibility**, not just cleanliness.

---

## ETL vs ELT Summary

| Aspect | ETL | ELT |
|------|-----|-----|
| Transform timing | Before load | After load |
| Data stored | Clean only | Raw + processed |
| Schema | Fixed | Flexible |
| ML suitability | Low | High |

---

## Key Takeaway
Modern ML systems almost always follow **ELT**, with transformations happening close to model training and inference.

---

## Resources
- Blog: ETL vs ELT Explained – Snowflake  
- YouTube: ETL vs ELT – Seattle Data Guy  
- Article: Why ELT is Better for ML Pipelines
