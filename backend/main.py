from fastapi import FastAPI


from backend.schema import CustomerRequest

from backend.models import predict_customer
from etl.transform import transform_customer

app = FastAPI()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer Churn API Running"}


@app.post("/predict")
def predict(data: CustomerRequest):
    result = predict_customer(data)

    return result
from sqlalchemy import text
from backend.database import engine

@app.get("/predictions")
def get_predictions():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT *
                FROM predictions
                ORDER BY id DESC
                """
            )
        )

        rows = result.mappings().all()

    return rows