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

Example: load_data → validate_data → train_model

---

## 2️⃣ Tasks

A task is a single unit of work.

Good tasks:
- load_data
- validate_data
- train_model

Bad task:
- load + validate + train in one function

Tasks should be:
- Independent
- Retryable
- Idempotent

---

## 3️⃣ Scheduling

Defines when the pipeline runs.

Examples:
- `@daily`
- `@hourly`
- Cron format
- Manual trigger

---

## 4️⃣ Retries

If a task fails:
- Automatically retry
- Wait before retrying
- Fail after max attempts

Important for:
- Network issues
- Temporary DB failures

---

## 5️⃣ Backfills

Run pipeline for past dates.

Example: Process data from 2024-01-01 to 2024-01-10


Critical for:
- Historical ML training
- Reprocessing old data

---


## Install Airflow

```bash
pip install apache-airflow





