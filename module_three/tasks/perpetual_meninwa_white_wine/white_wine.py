from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Let us load our saved model
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# Let us initialize our application
app = FastAPI()

# Let us create our pydantic model for validation
class WineFeatures(BaseModel):
  fixed_acidity: float
  volatile_acidity: float
  citric_acid: float
  residual_sugar: float
  chlorides: float
  free_sulfur_dioxide: float
  total_sulfur_dioxide: float
  density: float
  pH: float
  sulphates: float
  alcohol: float

# root endpoint
@app.get('/')
def home():
  return {
    "message": "Welcome to Wine Quality Prediction App... 🍷🍷🍷"
  }

# prediction endpoint
# convert the features to a 2D numpy array using [[]]
@app.post('/predict')
def predict(wine: WineFeatures):
  features = np.array([[
    wine.fixed_acidity,
    wine.volatile_acidity,
    wine.citric_acid,
    wine.residual_sugar,
    wine.chlorides,
    wine.free_sulfur_dioxide,
    wine.total_sulfur_dioxide,
    wine.density,
    wine.pH,
    wine.sulphates,
    wine.alcohol,
  ]])

  # Let us scale our input features using the loaded scaler (to normalize the input)
  scaled_features = scaler.transform(features)

  # Let us make prediction with the loaded model
  prediction = model.predict(scaled_features)

  # return the prediction - and the prediction converted to string for serialization
  return {"predicted_quality": str(prediction[0])}

# Run prediction with "uvicorn white_wine:app --reload"
