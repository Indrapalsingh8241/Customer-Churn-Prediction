# Customer-Churn-Prediction
# 📉 Customer Churn Prediction Platform

An end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn using historical customer data.

The project includes:

* Data preprocessing and feature engineering
* Machine Learning model training
* FastAPI backend
* PostgreSQL database integration
* Streamlit frontend dashboard
* Docker containerization

---

## 🚀 Features

### Machine Learning

* Customer churn prediction using Logistic Regression
* Probability score generation
* Feature engineering pipeline
* One-hot encoding for categorical features

### Backend

* FastAPI REST API
* Pydantic request validation
* Model inference endpoint
* Prediction history endpoint

### Database

* PostgreSQL integration using SQLAlchemy
* Stores prediction history
* Tracks customer churn probabilities

### Frontend

* Streamlit dashboard
* Interactive customer input form
* Churn probability visualization
* Prediction history dashboard

### Deployment Ready

* Dockerized backend
* Environment variable configuration
* Production-ready project structure

---

# 📂 Project Structure

```text
customer_churn_platform/

├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schema.py
│   └── save_prediction.py
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── frontend/
│   └── app.py
│
├── notebook/
│   ├── churn_prediction.ipynb
│   └── churn_model.pkl
│
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

# ⚙️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib

### Backend

* FastAPI
* Pydantic
* SQLAlchemy

### Database

* PostgreSQL

### Frontend

* Streamlit

### DevOps

* Docker
* Git
* GitHub

---

# 🧠 Feature Engineering

The following engineered features are created during preprocessing:

* is_new_customer
* high_monthly_charge
* Service_Count
* charges_per_service
* security_support_score
* Tenure_MonthlyCharges_Interaction

---

# 📡 API Endpoints

## Predict Customer Churn

```http
POST /predict
```

### Sample Request

```json
{
  "customerID": "TEST001",
  "gender": "Female",
  "SeniorCitizen": 1,
  "Partner": "No",
  "Dependents": "No",
  "tenure": 1,
  "PhoneService": "Yes",
  "MultipleLines": "Yes",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 105.50,
  "TotalCharges": 105.50
}
```

### Sample Response

```json
{
  "churn": "Yes",
  "churn_probability": 0.81
}
```

---

## Get Previous Predictions

```http
GET /predictions
```

Returns all predictions stored in PostgreSQL.

---

# 🗄️ Database Schema

## predictions

| Column            | Type    |
| ----------------- | ------- |
| id                | SERIAL  |
| customer_id       | VARCHAR |
| prediction        | VARCHAR |
| churn_probability | FLOAT   |

---

# 🐳 Docker

Build Image

```bash
docker build -t churn-api .
```

Run Container

```bash
docker run -p 8000:8000 \
-e DATABASE_URL=<your_database_url> \
churn-api
```

---

# ▶️ Running Locally

## Start Backend

```bash
uvicorn backend.main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Start Frontend

```bash
streamlit run frontend/app.py
```

Dashboard:

```text
http://localhost:8501
```

---

# 📊 Model Performance

| Metric   | Score |
| -------- | ----- |
| Accuracy | ~80%  |
| ROC-AUC  | ~84%  |

---

# 🎯 Future Improvements

* SHAP Explainability
* CatBoost/XGBoost Comparison
* User Authentication
* Cloud Deployment
* Prediction Analytics Dashboard
* CI/CD Pipeline

---

# 👨‍💻 Author

Indrapal Singh

Machine Learning | Data Science | Backend Development

Built as an end-to-end production-style ML project using FastAPI, PostgreSQL, Streamlit, and Docker.
