import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('churn_model.pkl', 'rb'))

st.title("📱 Telco Customer Churn Prediction")

# Input fields
senior = st.selectbox("Senior Citizen?", [0, 1])
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

# Predict
if st.button("Predict"):
    try:
        # Ensure proper types
        senior = int(senior)
        monthly = float(monthly)
        total = float(total)

        # Predict
        result = model.predict([[senior, monthly, total]])
        st.success("Prediction: {}".format("Churn" if result[0] == 1 else "No Churn"))

    except Exception as e:
        st.error(f"Error during prediction: {e}")


