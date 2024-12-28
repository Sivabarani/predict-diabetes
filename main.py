import streamlit as st
import numpy as np
import pickle

with open('./model_3.pkl', 'rb') as file:
    result = pickle.load(file)

st.title("Predict Diabetes")
name = st.text_input("Enter Name")

option_gender = st.selectbox('Select Gender', ['Select gender', 'Male', 'Female', 'Other'])

#input_age = st.number_input("Enter Age",  min_value=0.0, max_value=120.0, step=0.5)
option_age = st.select_slider('Select Age', list(range(1, 121)))

option_hypertension = st.selectbox("Select Hypertension", ['Select Hypertension', 'Yes', 'No'])

option_heart_disease = st.selectbox("Select Heart Disease", ['Select Heart Disease','Yes', 'No'])

option_smoking_history = st.selectbox("Select Smoking Habit", ['Never', 'No Info', 'Current', 'Former', 'Ever', 'Not Current'])

option_bmi = st.number_input('Enter BMI')

option_hba1_level = st.number_input('Enter HbA1 Level')

option_glucose = st.number_input('Enter Blood Glucose Level', min_value=0, max_value=300, step=1)

def form_data(gender, age, hypertendion, heart_disease, smoking, bmi, hba1_level, glucose):
    gender_dict = { 'Female': 0, 'Male' : 1, 'Other': 2}
    tension_and_disease_dict = {'Yes': 1, 'No': 0 }
    smoke_dict = {
        'No Info': 0,
        'Current': 1,
        'Ever': 2,
        'Former': 3,
        'Never': 4,
        'Not Current': 5
     }
    
    list_data = []
    if gender:
        list_data.append(gender_dict.get(gender))
    
    if age:
        list_data.append(age)

    if hypertendion:
        list_data.append(tension_and_disease_dict.get(hypertendion))

    if heart_disease:
        list_data.append(tension_and_disease_dict.get(heart_disease))

    if smoking:
        list_data.append(smoke_dict.get(smoking))

    if bmi:
        list_data.append(bmi)

    if hba1_level:
        list_data.append(hba1_level)

    if glucose:
        list_data.append(glucose)

    return list_data

if st.button("Predict Diabetes"):
    current_date = form_data(option_gender, option_age, option_hypertension, option_heart_disease, option_smoking_history, 
                            option_bmi,  option_hba1_level, option_glucose)
    input_data = np.array([current_date])

    prediction = result.predict(input_data)

    if prediction[0] == 1:
        st.success(f"{name}, based on the information you provided, there is an indication of a potential risk of diabetes.")
        st.success("However, this is not a definitive diagnosis. We highly recommend consulting with a healthcare professional for further evaluation and guidance.")
    else:
        st.success(f"Good news, {name}! Based on your inputs, the prediction suggests a lower likelihood of diabetes.")
        st.success("However, this is not conclusive. We recommend speaking with a doctor to confirm and discuss your health in detail.")