import streamlit as st
from deployment import predict_page
from explore import show_explore

page = st.sidebar.selectbox("Explore or predict",("Predict","Explore"))

if page == "Predict":
    predict_page()
else:
    show_explore()




