# ML Production Pipeline with Airflow

## 📌 Project Overview

This project demonstrates how to build a **production-style Machine Learning pipeline** using:

- Apache Airflow (workflow orchestration)
- Python (ML logic)
- Pandas (data processing)
- Scikit-learn (model training)
- Joblib (model saving)
- Linux (WSL environment)
- Virtual environments (dependency isolation)

The goal was to move from notebook-based ML to **system-level ML engineering**.

---

## 🧠 What This Pipeline Does

The pipeline performs the following steps:

1. Extract data from CSV
2. Validate data (fail-fast approach)
3. Train a machine learning model
4. Save versioned model artifacts
5. Orchestrate the entire workflow using Airflow

---

## 🏗 Project Structure

```
airflow_project/
│
├── airflow_env/               # Python virtual environment
│
├── data/
│   └── sample_data.csv        # Input dataset
│
├── models/
│   └── model_*.pkl            # Versioned trained models
│
├── src/
│   └── ml_pipeline.py         # ML logic (extract, validate, train)
│
└── ~/airflow/
    └── dags/
        └── ml_pipeline.py     # Airflow DAG (orchestration)
```

---

## 📂 Dataset Used

File: `data/sample_data.csv`

```
age,salary,target
25,50000,0
30,60000,1
45,80000,1
22,40000,0
```

- `age` → Feature  
- `salary` → Feature  
- `target` → Label  

---

## ⚙️ ML Logic (src/ml_pipeline.py)

### 1️⃣ Extract

- Reads CSV using Pandas
- Stores intermediate data as `/tmp/data.pkl`

```python
df = pd.read_csv(DATA_PATH)
df.to_pickle("/tmp/data.pkl")
```

Why?  
Airflow tasks are isolated. We pass data via temporary storage.

---

### 2️⃣ Validate (Fail-Fast Design)

Checks:

- No null values
- Required columns exist
- Feature columns present

```python
if df.isnull().sum().sum() > 0:
    raise ValueError("Dataset contains null values!")
```

If validation fails:
- Pipeline stops
- Training does not run

---

### 3️⃣ Train Model

- Uses Logistic Regression
- Trains on features: age, salary
- Saves model with timestamp

```python
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_path = os.path.join(MODEL_DIR, f"model_{timestamp}.pkl")
joblib.dump(model, model_path)
```

Each pipeline run creates:

```
model_20260223_104700.pkl
```

This ensures **model versioning**.

---

## 🔄 Airflow DAG (Orchestration Layer)

The DAG defines execution order:

```
extract_data → validate_data → train_model
```

If validation fails:
- Training never runs
- DAG run fails

Airflow handles:
- Task scheduling
- Retries
- Logging
- Monitoring
- Dependency management

---

## 🚀 How to Run the Pipeline

### 1️⃣ Activate Virtual Environment

```bash
cd ~/airflow_project
source airflow_env/bin/activate
```

### 2️⃣ Start Airflow

```bash
airflow standalone
```

### 3️⃣ Open Airflow UI

Open browser:

```
http://localhost:8080
```

### 4️⃣ Trigger DAG

- Enable `ml_production_pipeline`
- Click "Trigger DAG"
- Monitor Graph View

---

## 📦 Output

After successful run:

```bash
ls ~/airflow_project/models
```

Example output:

```
model_20260223_104624.pkl
model_20260223_104700.pkl
```

Each file represents a versioned trained model.

---

## 🔥 Key Concepts Learned

### ✅ Virtual Environments
Airflow only sees packages installed inside the active virtual environment.

### ✅ Airflow Home
DAGs must be placed in:

```
$AIRFLOW_HOME/dags
```

### ✅ Separation of Concerns
- Airflow → Orchestration
- src/ → ML logic
- data/ → Input
- models/ → Output

### ✅ Fail-Fast Validation
Data validation stops bad data before training.

### ✅ Model Versioning
Each training run produces a unique timestamped artifact.

---

## 🏁 What This Project Represents

This is no longer notebook experimentation.

It is a structured ML system that:

- Runs tasks in defined order
- Stops on failure
- Saves versioned artifacts
- Can be scheduled daily
- Mimics real production ML pipelines

---

## 📈 Possible Improvements

- Add model evaluation task
- Integrate Great Expectations
- Add MLflow experiment tracking
- Add data drift detection
- Dockerize the project
- Add CI/CD pipeline
- Deploy trained model as API

---

## 🎯 Conclusion

This project marks the transition from:

"Training models in notebooks"

to

"Building production-ready ML pipelines using orchestration."

You now understand how real-world ML systems are structured.
