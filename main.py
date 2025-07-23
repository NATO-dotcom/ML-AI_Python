import os
print("Current working directory:", os.getcwd())

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

#load models
model_duration = joblib.load("model_duration.pkl")
model_method = joblib.load("model_method.pkl")

#load label encoders
encoders = {
    'subject_type': joblib.load("le_subject_type.pkl"),
    'time_of_day': joblib.load("le_time_of_day.pkl"),
    'prev_method_used': joblib.load("le_prev_method_used.pkl"),
    'mood': joblib.load("le_mood.pkl"),
    'user_type': joblib.load("le_user_type.pkl"),
    'recommended_method': joblib.load("le_recommended_method.pkl"),
}
#input schema
class UserInput(BaseModel):
    subject_type: str
    time_of_day: str
    focus_score: int
    task_difficulty: int
    prev_method_used: str
    mood: str
    user_type: str

@app.post("/recommend")
def get_recommendation(data: UserInput):
    input_data = pd.DataFrame([[
        encoders['subject_type'].transform([data.subject_type])[0],
        encoders['time_of_day'].transform([data.time_of_day])[0],
        data.focus_score,
        data.task_difficulty,
        encoders['prev_method_used'].transform([data.prev_method_used])[0],
        encoders['mood'].transform([data.mood])[0],
        encoders['user_type'].transform([data.user_type])[0]
    ]], columns=[
        'subject_type', 'time_of_day', 'user_focus_score',
        'task_difficulty', 'prev_method_used', 'mood', 'user_type'
    ])

    duration = int(model_duration.predict(input_data)[0])
    method_encoded = model_method.predict(input_data)[0]
    method = encoders['recommended_method'].inverse_transform([method_encoded])[0]

    return {
        "recommended_duration": duration,
        "recommended_method": method
    }