import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('churn_model.pkl', 'rb'))

st.title("📱 Telco Customer Churn Prediction")

# Take simple inputs
senior = st.selectbox("Senior Citizen?", [0, 1])
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

# Predict
if st.button("Predict"):
    result = model.predict([[senior, monthly, total]])
    st.success("Prediction: {}".format("Churn" if result[0] == 1 else "No Churn"))

