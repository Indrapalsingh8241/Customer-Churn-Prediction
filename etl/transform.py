import pandas as pd

def transform_customer(customer):

    

    df = pd.DataFrame(
    [customer.dict()]
)

    # engineered features

    df["is_new_customer"] = (
        df["tenure"] < 12
    ).astype(int)

    df["high_monthly_charge"] = (
        df["MonthlyCharges"] > 70
    ).astype(int)

    df["Tenure_MonthlyCharges_Interaction"] = (
        df["tenure"] *
        df["MonthlyCharges"]
    )

    services = [
        "PhoneService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    service_count = 0

    for col in services:

        if df.loc[0, col] == "Yes":
            service_count += 1

    df["Service_Count"] = service_count

    df["charges_per_service"] = (
        df["MonthlyCharges"] /
        max(service_count, 1)
    )

    security_score = 0

    if df.loc[0, "OnlineSecurity"] == "Yes":
        security_score += 1

    if df.loc[0, "TechSupport"] == "Yes":
        security_score += 1

    df["security_support_score"] = security_score

    categorical_columns = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod"
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_columns
    )

    return df