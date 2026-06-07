import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="wide"
)

st.title("📉 Customer Churn Prediction Platform")

st.markdown(
    "Predict whether a customer is likely to churn using Machine Learning."
)

# ======================
# Customer Information
# ======================

st.header("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    customerID = st.text_input("Customer ID")
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    SeniorCitizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

with col2:
    tenure = st.number_input(
        "Tenure",
        min_value=0,
        value=12
    )

    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )

# ======================
# Account Information
# ======================

st.header("🏠 Account Information")

col1, col2 = st.columns(2)

with col1:
    Partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

with col2:
    Contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

# ======================
# Services
# ======================

st.header("📞 Services")

col1, col2 = st.columns(2)

with col1:
    PhoneService = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    MultipleLines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    InternetService = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    OnlineSecurity = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col2:
    DeviceProtection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    TechSupport = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    StreamingTV = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    StreamingMovies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

# ======================
# Billing
# ======================

st.header("💳 Billing Information")

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# ======================
# Prediction
# ======================

if st.button("🚀 Predict Churn", use_container_width=True):

    payload = {
        "customerID": customerID,
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    result = response.json()

    st.divider()

    st.subheader("📊 Prediction Result")

    prob = result["churn_probability"]

    if result["churn"] == "Yes":
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")

    if prob >= 0.7:
        st.error(f"🔴 High Risk ({prob:.2%})")

    elif prob >= 0.4:
        st.warning(f"🟡 Medium Risk ({prob:.2%})")

    else:
        st.success(f"🟢 Low Risk ({prob:.2%})")

    st.progress(int(prob * 100))

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Churn Probability",
            f"{prob*100:.2f}%"
        )

    with col2:
        st.metric(
            "Prediction",
            result["churn"]
        )
    st.subheader("💡 Why this prediction?")

    for reason in result["reasons"]:
        st.write("•", reason)

    st.info(
            f"""
        Customer ID: {customerID}

    Predicted Churn: {result['churn']}

            Probability: {prob:.2%}
"""
    )
st.divider()

st.header("📊 Previous Predictions")

response = requests.get(
    "http://127.0.0.1:8000/predictions"
)

if response.status_code == 200:

    predictions = response.json()

    if predictions:

        import pandas as pd

        df = pd.DataFrame(predictions)
        if not df.empty:

            total = len(df)

        churn_yes = len(
        df[df["prediction"] == "Yes"]
    )

        churn_no = len(
        df[df["prediction"] == "No"]
    )

        col1, col2, col3 = st.columns(3)

        col1.metric(
        "Total Predictions",
        total
    )

        col2.metric(
        "Churn Yes",
        churn_yes
    )

        col3.metric(
        "Churn No",
        churn_no
    )



        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No predictions found."
        )
    