import re
import joblib
import numpy as np

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('_'),
        url.count('/'),
        url.count('?'),
        url.count('='),
        url.count('@'),
        url.count('&'),
        url.count('//')  # redirection
    ]

def load_model_and_scaler(model_path='model/xgboost.pkl', scaler_path='model/scaler.pkl'):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

def predict_url(url, model, scaler):
    features = extract_features(url)
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)[0]
    proba = model.predict_proba(scaled_features)[0].max()
    return prediction, proba
