
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
# 📊 Model Performance

Three machine learning models were evaluated for customer churn prediction.

| Model               | Accuracy   | Precision  | Recall     | F1 Score   | ROC-AUC    |
| ------------------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| Logistic Regression | **80.70%** | **66.35%** | **55.35%** | **60.35%** | **84.32%** |
| XGBoost             | 79.49%     | 63.93%     | 52.14%     | 57.44%     | 83.47%     |
| Random Forest       | 79.13%     | 63.61%     | 50.00%     | 55.99%     | 82.51%     |

## Model Selection

After evaluating multiple machine learning algorithms, Logistic Regression was selected as the final production model because it achieved the best overall performance across all major evaluation metrics.

### Final Model (Logistic Regression)

* Accuracy: 80.70%
* Precision: 66.35%
* Recall: 55.35%
* F1 Score: 60.35%
* ROC-AUC: 84.32%

The model demonstrates strong predictive capability for identifying customers at risk of churn while maintaining a balance between precision and recall.

---

# 🔍 Key Churn Drivers

Feature importance analysis identified the following factors as the strongest indicators of customer churn:

| Rank | Feature                        | Importance |
| ---- | ------------------------------ | ---------- |
| 1    | Contract_Month-to-month        | 0.2500     |
| 2    | is_new_customer                | 0.1165     |
| 3    | InternetService_Fiber optic    | 0.0951     |
| 4    | OnlineSecurity_No              | 0.0496     |
| 5    | InternetService_DSL            | 0.0301     |
| 6    | Contract_Two year              | 0.0293     |
| 7    | TechSupport_No                 | 0.0290     |
| 8    | PhoneService_Yes               | 0.0198     |
| 9    | StreamingMovies_Yes            | 0.0194     |
| 10   | PaymentMethod_Electronic check | 0.0188     |

### Business Insights

Customers are more likely to churn when they:

* Use a Month-to-Month contract
* Are new customers
* Use Fiber Optic internet services
* Do not subscribe to Online Security
* Do not have Technical Support
* Pay via Electronic Check

Customers are less likely to churn when they:

* Have long-term contracts (One Year or Two Year)
* Subscribe to Online Security services
* Subscribe to Technical Support services
* Have longer customer tenure

These insights can help telecom companies design targeted customer retention strategies and reduce customer attrition.


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
