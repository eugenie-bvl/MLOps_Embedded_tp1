import streamlit as st
import joblib
import numpy as np

model = joblib.load("regression.joblib") 

# Using the st.number_input function
# create three form fields for size
# number of bedrooms and whether a house has a garden
# st.number_input("Insert the size: ")
with st.form("my_form"):
    st.title("House Regression")
    size_val = st.number_input("Insert the size :")
    bedroom_val = st.number_input("Insert the number of bedroom :")
    garden_val = st.checkbox("Has a garden : ")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        features = np.array([[size_val, bedroom_val, garden_val]])
        prediction = model.predict(features)
        st.write(f"Predicted price: {prediction[0]}")

