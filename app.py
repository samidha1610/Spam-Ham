import streamlit as st
import joblib
model = joblib.load('Email_Class')
st.title("Spam Ham Classifier")
ip = st.text_input("Enter your Message ")
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
