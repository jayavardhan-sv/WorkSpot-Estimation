from unittest import result

import streamlit as st
import pandas as pd
import joblib

# Load model and encoders

model = joblib.load("workspot_model.pkl")
gender_encoder = joblib.load("gender_encoder.pkl")
dept_encoder = joblib.load("dept_encoder.pkl")
target_encoder = joblib.load("target_encoder.pkl")

st.set_page_config(
page_title="WorkSpot Preference Estimation",
page_icon="🏢",
layout="centered"
)

st.title("🏢 WorkSpot Preference Estimation")
st.write(
"Predict the most suitable workplace preference using Machine Learning."
)

# User Inputs

age = st.number_input(
"Age (20-60)",
min_value=20,
max_value=60,
value=30
)

gender = st.selectbox(
"Gender",
["Male", "Female"]
)

working_hours = st.slider(
"Working Hours (4-12)",
min_value=4,
max_value=12,
value=8
)

commute_time = st.number_input(
"Commute Time (minutes) (0-180)",
min_value=0,
max_value=180,
value=30
)

distance = st.number_input(
"Distance from Home (km) (0-100)",
min_value=0,
max_value=100,
value=10
)

experience = st.number_input(
"Work Experience (years) (0-40)",
min_value=0,
max_value=40,
value=5
)

department = st.selectbox(
"Department",
["IT", "HR", "Sales", "Finance", "Marketing", "Operations"]
)

wlb_score = st.slider(
"Work-Life Balance Score",
min_value=1,
max_value=10,
value=7
)

if st.button("Predict Workplace"):

    gender_encoded = gender_encoder.transform([gender])[0]
    department_encoded = dept_encoder.transform([department])[0]

    input_df = pd.DataFrame({
        "Age": [age],
        "Gender": [gender_encoded],
        "Working_Hours": [working_hours],
        "Commute_Time": [commute_time],
        "Distance_from_Home": [distance],
        "Work_Experience": [experience],
        "Department": [department_encoded],
        "Work_Life_Balance_Score": [wlb_score]
    })

    prediction = model.predict(input_df)
    
    workplace = target_encoder.inverse_transform(prediction)[0]

    st.success(f"Workplace : {workplace}")
    st.subheader("Input Summary")
    st.dataframe(input_df)
