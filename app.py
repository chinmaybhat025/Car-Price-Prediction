# Flask code
# from flask import Flask, render_template, request
# import jsonify
# import requests
# import pickle
# import numpy as np
# import sklearn
# from sklearn.preprocessing import StandardScaler
# app = Flask(__name__)
# model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
# @app.route('/',methods=['GET'])
# def Home():
#     return render_template('index.html')
#
#
# standard_to = StandardScaler()
# @app.route("/predict", methods=['POST'])
# def predict():
#     Fuel_Type_Diesel=0
#     if request.method == 'POST':
#         Year = int(request.form['Year'])
#         Present_Price=float(request.form['Present_Price'])
#         Kms_Driven=int(request.form['Kms_Driven'])
#         Owner=int(request.form['Owner'])
#         Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
#         if(Fuel_Type_Petrol=='Petrol'):
#                 Fuel_Type_Petrol=1
#                 Fuel_Type_Diesel=0
#         elif(Fuel_Type_Petrol=='Diesel'):
#             Fuel_Type_Petrol=0
#             Fuel_Type_Diesel=1
#         else:
#             Fuel_Type_Petrol=0
#             Fuel_Type_Diesel=0
#
#         Year=2024-Year
#         Seller_Type_Individual=request.form['Seller_Type_Individual']
#         if(Seller_Type_Individual=='Individual'):
#             Seller_Type_Individual=1
#         else:
#             Seller_Type_Individual=0
#         Transmission_Mannual=request.form['Transmission_Mannual']
#         if(Transmission_Mannual=='Mannual'):
#             Transmission_Mannual=1
#         else:
#             Transmission_Mannual=0
#         prediction=model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
#         output=round(prediction[0],2)
#         if output<0:
#             return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
#         else:
#             return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
#     else:
#         return render_template('index.html')
#
# if __name__=="__main__":
#     app.run(debug=True)
#


import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

# Set up the Streamlit app layout
st.title('Car Price Prediction')

# Input fields for user data
Year = st.number_input('Year', min_value=1900, max_value=2024)
Present_Price = st.number_input('Present Price')
Kms_Driven = st.number_input('Kms Driven')
Owner = st.number_input('Owner', min_value=0)

# Fuel Type selection
Fuel_Type_Petrol = st.selectbox('Fuel Type', ['Petrol', 'Diesel'])
if Fuel_Type_Petrol == 'Petrol':
    Fuel_Type_Diesel = 0
    Fuel_Type_Petrol = 1
else:
    Fuel_Type_Diesel = 1
    Fuel_Type_Petrol = 0

# Seller Type selection
Seller_Type_Individual = st.selectbox('Seller Type', ['Individual', 'Dealer'])
if Seller_Type_Individual == 'Individual':
    Seller_Type_Individual = 1
else:
    Seller_Type_Individual = 0

# Transmission selection
Transmission_Mannual = st.selectbox('Transmission', ['Mannual', 'Automatic'])
if Transmission_Mannual == 'Mannual':
    Transmission_Mannual = 1
else:
    Transmission_Mannual = 0

# Prediction logic
if st.button('Predict'):
    # Calculate the year difference for the model input
    Year = 2024 - Year

    # Make prediction
    prediction = model.predict([[Present_Price, Kms_Driven, Owner, Year,
                                 Fuel_Type_Diesel, Fuel_Type_Petrol,
                                 Seller_Type_Individual, Transmission_Mannual]])

    output = round(prediction[0], 2)

    if output < 0:
        st.error("Sorry, you cannot sell this car.")
    else:
        st.success(f"You can sell the car at ₹{output}")


