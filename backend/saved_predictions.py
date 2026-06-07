from backend.database import engine
from sqlalchemy import MetaData, Table

metadata = MetaData()

predictions = Table(
    "predictions",
    metadata,
    autoload_with=engine
)

def save_prediction(
    customer_id,
    prediction,
    churn_probability
):
    churn_label = "Yes" if prediction == 1 else "No"
    with engine.connect() as conn:

        stmt = predictions.insert().values(
            customer_id=customer_id,
            prediction=churn_label,
            churn_probability=churn_probability
        )

        conn.execute(stmt)
        conn.commit()