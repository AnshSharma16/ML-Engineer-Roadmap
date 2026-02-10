# CI/CD for ML Pipelines

## Why CI/CD is needed in ML

ML systems require CI/CD to automatically validate:
- Data quality
- Training pipelines
- Inference safety

CI ensures unsafe changes never reach production.

---

## CI in This Project

This project uses GitHub Actions to:
- Install dependencies
- Run data validation
- Run training pipeline sanity checks

CI is triggered on every push or pull request.
