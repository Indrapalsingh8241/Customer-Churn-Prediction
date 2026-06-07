
import pandas as pd
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "etl" / "churn_model.pkl"

model = joblib.load(MODEL_PATH)
from etl.transform import transform_customer
from backend.saved_predictions import save_prediction

def predict_customer(customer):

    df = transform_customer(customer)

    df = df.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    prediction =int( model.predict(df)[0])

    probability = float(model.predict_proba(df)[0][1])
    
    
    save_prediction(
        customer_id=customer.customerID,
        prediction=prediction,
        churn_probability=probability
    )
    reasons = []

    
    

    if df.loc[0, "Contract_Month-to-month"] == 1:
     reasons.append(
        "Month-to-month contract customers tend to churn more frequently."
    )

    if df.loc[0, "PaymentMethod_Electronic check"] == 1:
     reasons.append(
        "Electronic check payment method is associated with higher churn."
    )

    if df.loc[0, "InternetService_Fiber optic"] == 1:
     reasons.append(
        "Fiber optic customers historically show higher churn rates."
    )

    if df.loc[0, "OnlineSecurity_No"] == 1:
        reasons.append(
        "Customer does not have online security services."
    )

    if df.loc[0, "TechSupport_No"] == 1:
        reasons.append(
        "Customer does not have technical support services."
    )

    if df.loc[0, "is_new_customer"] == 1:
        reasons.append(
        "Customer is relatively new."
    )

    if df.loc[0, "high_monthly_charge"] == 1:
        reasons.append(
        "Monthly charges are relatively high."
    )

    if df.loc[0, "security_support_score"] == 0:
        reasons.append(
        "Customer lacks both security and support services."
    )
    
    churn_label = "Yes" if prediction == 1 else "No"
    return {
        "customer_id": customer.customerID,
        "churn" : churn_label,

        "churn_probability": probability,
          "reasons": reasons
    }