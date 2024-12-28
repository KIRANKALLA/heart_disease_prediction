import streamlit as st
import joblib
m = joblib.load('hdp_model.joblib')

st.title('Heart Disease Prediction')
st.write('Enter Features such as Age,Gender Etc;;')

a = st.number_input('Enter Age')
b = st.number_input('Enter Cigarettes Per Day')
c = st.number_input('Total Cholestrol')
d = st.number_input('Enter Systolic BP')
e = st.number_input('Enter Diastolic BP')
f = st.number_input('Enter BODY MASS INDEX')
g = st.number_input('Enter Heart Rate')
h = st.number_input('Enter Glucose')

if st.button('Predict'):
    p = m.predict([[a,b,c,d,e,f,g,h]])
    if p==0:
        st.write('You Will Have Heart Disease in the Next 10 years')
    else:
        st.write('You Will not Have Heart Disease in the Next 10 Years')

