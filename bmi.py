import streamlit as st
import pandas as pd

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kg", min_value=0.0, step=0.1)
status = st.radio("Select your height format", ('cms', 'meters', 'feet'))

try:
    if status == 'cms':
        height = st.number_input('Centimeters')
        bmi = weight/((height/100)**2)

    elif status == 'meters':
        height = st.number_input('meters')
        bmi = weight/(height**2)
    else :
        height = st.number_input('meters')
        bmi = weight/((height/3.28)**2)
except:
    print('zero division error')

if(st.button('Calculate BMI')):
    st.write(f'Your BMI index is {round(bmi)}')

    if bmi<18.5:
        st.warning('You are underweight')
    elif (bmi>=18.5 and bmi<=24.9):
        st.success('You are Healthy')
    elif (bmi>=24.9 and bmi<=29.9):
        st.error('You are Overweight')
    elif (bmi>30):
        st.warning('You are extremely overweight')
