# 💳 UPI Fraud Detection using Machine Learning

A smart ML-powered web app to detect potential UPI transaction fraud in real-time. Built with Flask, this app uses advanced classification techniques to evaluate the likelihood of fraudulent behavior based on transaction patterns and user behavior.

---

## 🔍 Features

- ✅ Fraud classification with probability score  
- 📊 Supports multiple input features including location, device, and transaction type  
- 🎯 XGBoost model tuned for high accuracy with SMOTE for class balancing  
- 🌐 User-friendly web interface built with Flask and HTML/CSS  
- ⚠️ Instant visual feedback: 🔴 Fraudulent or 🟢 Legitimate  

---

## 🧠 Model

The model uses:
- 📈 XGBoost (best performer)  
- 🧪 Compared with Logistic Regression, SVM, KNN, Random Forest, CNN, etc.  
- 🧬 Feature engineering with Chi-Square, ANOVA  
- 🧰 Balanced using SMOTE, scaled via StandardScaler  
- 🔧 Tuned via GridSearchCV  

---

## 📥 Dataset

We used this public dataset from Kaggle for training and testing:

📂 [Fraud UPI Transaction Details – Kaggle](https://www.kaggle.com/datasets/iamravi11/fraud-upi-transaction-details)

It contains realistic transaction patterns with features like:
- Amount, MerchantCategory, TransactionType  
- Geo-location, Device info, User behavior  
- Fraudulent labels

---

## 📥 Input Features

| Feature                | Description                            |
|------------------------|----------------------------------------|
| Amount                | Transaction amount                     |
| MerchantCategory      | Type of merchant (Electronics, Food...)|
| TransactionType       | P2P / P2M                              |
| Latitude & Longitude  | Geolocation of transaction             |
| AvgTransactionAmount  | User’s average transaction amount      |
| TransactionFrequency  | Number of transactions per day         |
| UnusualLocation       | 1 if location is unusual               |
| UnusualAmount         | 1 if amount is higher than usual       |
| NewDevice             | 1 if accessed from a new device        |
| FailedAttempts        | Number of failed login/payment attempts|
| BankName              | Bank handling the transaction          |

---

## ⚙️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Azzanraj/upi-fraud-detection.git
   cd upi-fraud-detection
