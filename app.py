from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load scaler and trained model
scaler = joblib.load("scaler.pkl")
model = joblib.load("xgb_model.pkl")  # Your best XGBoost model

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form

        features = [
            float(data['Amount']),
            int(data['MerchantCategory']),
            int(data['TransactionType']),
            float(data['Latitude']),
            float(data['Longitude']),
            float(data['AvgTransactionAmount']),
            int(data['TransactionFrequency']),
            int(data['UnusualLocation']),
            int(data['UnusualAmount']),
            int(data['NewDevice']),
            int(data['FailedAttempts']),
            int(data['BankName'])
        ]

        # Preprocess input
        scaled_input = scaler.transform([features])

        # Get prediction probability
        prob = model.predict_proba(scaled_input)[0][1]
        print(f"Fraud Probability: {prob:.4f}")

        # Use threshold for classification
        prediction = 1 if prob >= 0.3 else 0
        result = '🔴 Fraudulent Transaction' if prediction == 1 else '🟢 Legitimate Transaction'

        return render_template('result.html', result=result, probability=round(prob, 4))

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
