from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI(title="Laptop Price Prediction API")

with open("laptop_price_model.sav", "rb") as file:
    model = pickle.load(file)


@app.get("/")
def home():
    return {"message": "Laptop Price Prediction is Running"}


@app.post("/predict")
def predict(data: dict):

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)

    return {
        "prediction": float(prediction[0])
    }