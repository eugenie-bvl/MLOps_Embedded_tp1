from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    size_val: int
    bedroom_val: int
    garden_val: bool


model = joblib.load("regression.joblib")
app = FastAPI()

@app.get("/predict")
async def root():
    return {"y_pred": 2}

@app.post("/predict")
async def prediction(item: Item):
    features = np.array([[item.size_val, item.bedroom_val, item.garden_val]])
    prediction = model.predict(features)
    return {
        "predicted price": {prediction[0]}
    }
uvicorn.run(app, host="0.0.0.0", port=8023)