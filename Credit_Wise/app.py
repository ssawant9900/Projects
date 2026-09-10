import streamlit as st
import joblib

# Load saved files
model = joblib.load("loan_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
onehot_encoder = joblib.load("onehot_encoder.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="CreditWise", page_icon="🏦")

st.title("🏦 CreditWise")
st.subheader("Loan Approval Prediction System")

st.write("Predict whether a loan application is likely to be approved.")