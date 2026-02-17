# 1.5 Orchestration (Airflow / Prefect)

## 🎯 Goal
Learn how to build, schedule, retry, and monitor ML pipelines using orchestration tools like Airflow and Prefect.

---

# 📌 What is Orchestration?

Orchestration = Defining + Scheduling + Retrying + Monitoring workflows reliably.

Instead of manually running scripts, we define structured pipelines.

Example ML Pipeline:

Extract → Validate → Train → Evaluate → Save

---

# 🧠 Core Concepts

## 1️⃣ DAG (Directed Acyclic Graph)

- A workflow defined as ordered tasks
- Directed = tasks have order
- Acyclic = no loops

Example:

