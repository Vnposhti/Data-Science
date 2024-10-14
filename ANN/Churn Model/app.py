# Import Libraries

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle
import streamlit as st

# Import model, encoder and scalar
from tensorflow.keras.models import load_model
model = load_model('model.h5')

with open('geo.pkl','rb') as file:
    geo = pickle.load(file)

with open('gender.pkl','rb') as file:
    gender = pickle.load(file)

with open('scalar.pkl','rb') as file:
    scalar = pickle.load(file)

# Streamlit app
st.title('Churn Prediction')

# Customer Input for Streamlit
creditscore=st.slider('Credit Score',100,900,format="%d")
geography=st.selectbox('Geography',geo.columns)	
gender_st=st.selectbox('Gender',gender.classes_)
age=st.slider('Age',18,100)        
Tenure=st.slider('Tenure',0,10)
balance=st.number_input('Balance')
numofproducts=st.number_input('Number of Products',0,10,format="%d")
has_cr_card=st.selectbox('Has Credit Card',[0,1])
is_active_member=st.selectbox('Is active member',[0,1])
estimatedSalary=st.number_input('Estimated Salary')

# Prepare Input data
input_data = pd.DataFrame(
    {
        'CreditScore': [creditscore],
        'Gender': [gender.transform([gender_st])[0]],
        'Age': [age],
        'Tenure': [Tenure],
        'Balance': [balance],
        'NumOfProducts': [numofproducts],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimatedSalary]
    }
)

# Handle Geography using pd.get_dummies
geography_df = pd.get_dummies([geography],sparse=False, dtype='int', prefix='Geography')
geography_df = geography_df.reindex(columns=geo.columns, fill_value=0)  # Align with the geo.pkl structure

# Merge input data with geography dummy variables
input_data = pd.concat([input_data.reset_index(drop=True), geography_df], axis=1)

# Apply the scaler on the input data
input_data_scaled = scalar.transform(input_data)

# Predict churn using the loaded model
prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

# Display the result in Streamlit
st.write(f"Churn Prediction Probability: {prediction_proba:.2%}")

if prediction_proba>0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is not likely to churn.')