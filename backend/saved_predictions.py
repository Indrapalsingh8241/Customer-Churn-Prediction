from backend.database import engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Float,
    MetaData
)

metadata = MetaData()

predictions = Table(
    "predictions",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("customer_id", String(100)),
    Column("prediction", String(10)),
    Column("churn_probability", Float)
)

metadata.create_all(engine)

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