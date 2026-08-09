# 💻 Laptop Price Prediction

An end-to-end Machine Learning project that predicts laptop prices based on laptop specifications.

The project uses an **XGBoost Regressor** for prediction, **FastAPI** for the backend API, and **Streamlit** for the frontend interface.

The application is deployed online using **Render**.

---

## 🚀 Live Demo

### Frontend
https://laptop-price-frontend.onrender.com/

### Backend API
https://laptop-price-prediction-mbp5.onrender.com/

### API Documentation
https://laptop-price-prediction-mbp5.onrender.com/docs

---

## 🧠 Project Overview

The goal of this project is to predict the price of a laptop based on its specifications.

The user enters specifications such as:

- Company
- Product
- Laptop Type
- Screen Size
- RAM
- Operating System
- Weight
- Screen Type
- Screen Resolution
- Touchscreen
- IPS Panel
- Retina Display
- CPU Company
- CPU Frequency
- CPU Model
- Primary Storage
- Secondary Storage
- Storage Types
- GPU Company
- GPU Model

The trained XGBoost model then predicts the estimated laptop price.

---

## 🛠️ Technologies Used

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Deployment
- Render

### Version Control
- Git
- GitHub

---

## 📊 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Encoding Categorical Features
   ↓
Train-Test Split
   ↓
Model Training
   ↓
XGBoost Regressor
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
FastAPI Backend
   ↓
Streamlit Frontend