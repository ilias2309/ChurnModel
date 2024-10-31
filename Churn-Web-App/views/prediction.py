import streamlit as st
import pandas as pd
import joblib

# Load the model and data
model = joblib.load('C:/Users/Administrator/Desktop/ChurnModel/models/best_xgb_model.pkl')
encoder = joblib.load('C:/Users/Administrator/Desktop/ChurnModel/models/encoder.pkl')
data = pd.read_csv('C:/Users/Administrator/Desktop/ChurnModel/data/Bank Customer Churn Prediction.csv')

# Streamlit App Title
st.title("🚀 Bank Customer Churn Prediction")

st.markdown("""
Welcome to the **Bank Customer Churn Prediction** app. Please fill in the details below to predict whether a customer is likely to churn.
""")

# Two-column layout for the input fields
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)
    balance = st.number_input("Balance", min_value=0.0, value=50000.0)
    country = st.selectbox("Country", ['France', 'Germany', 'Spain'])

with col2:
    num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
    has_cr_card = st.selectbox("Has Credit Card?", ['Yes', 'No'])
    is_active_member = st.selectbox("Is Active Member?", ['Yes', 'No'])
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)
    gender = st.selectbox("Gender", ['Male', 'Female'])

# Collect user input into a DataFrame
user_input = pd.DataFrame({
    'CreditScore': [credit_score],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [1 if has_cr_card == 'Yes' else 0],
    'IsActiveMember': [1 if is_active_member == 'Yes' else 0],
    'EstimatedSalary': [estimated_salary],
    'country': [country],
    'gender': [gender]
})

# Manually encode categorical variables
user_input_encoded = pd.get_dummies(user_input, columns=['country', 'gender'])

# Align the input with the training data format
user_input_encoded = user_input_encoded.reindex(columns=encoder.get_feature_names_out(), fill_value=0)

# Predict churn probability and display a message
if st.button("Predict Churn"):
    prediction = model.predict(user_input_encoded)[0]

    if prediction == 1:
        st.markdown("<h3 style='color:red;'>Warning! This customer is likely to churn. Consider taking proactive measures to retain them.</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:green;'>Good news! This customer is not likely to churn. Keep up the good work in maintaining customer satisfaction.</h3>", unsafe_allow_html=True)

# Additional styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stNumberInput input, .stSelectbox select {
        background-color: #f0f0f5;
        border-radius: 5px;
        padding: 10px;
        color: #000000;  /* Ensure the input text is black */
    }
    .stNumberInput input::placeholder {
        color: #808080;  /* Ensure the placeholder text is gray and visible */
    }
</style>
""", unsafe_allow_html=True)
