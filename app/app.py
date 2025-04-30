from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model/iris_model.pkl")

class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class_labels = {0: "setosa", 1: "versicolor", 2: "virginica"}

@app.post("/predict")
def predict(data: InputData):
    features = [[
        data.sepal_length, data.sepal_width,
        data.petal_length, data.petal_width
    ]]
    prediction = model.predict(features)
    return {"prediction": class_labels[int(prediction[0])]}