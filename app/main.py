import pandas as pd
from fastapi import FastAPI # class
from app.models import load_model_scaler # Function
from app.schema import Cardio # class

app = FastAPI() # Object instance of FastAPI

model, scaler = load_model_scaler()

# request methods
# ------------------
# post(create/insert), get(read/retrive/select), put(udate, unique_id/PK), delete(remove, unique_id/PK)

@app.get('/')
def home():
    return 'Welcome to Cardiovascular disease prediction system'

@app.post('/predict-cardio')
def cardiovascular_prediction(data:Cardio):
    input_data = pd.DataFrame([
        data.model_dump() # From Schema to 2D List and model_dump -> Json -> Convertn
    ])
    input_scaler = scaler.transform(input_data)
    prediction = model.predict(input_scaler)[0]
    return {
        "Prediction_Status": int(prediction),
        "Status": "Likely To Be Healthy" if prediction == 0 else "Likely To Be UnHealthy"
    }