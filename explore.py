import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import warnings
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"
warnings.filterwarnings('ignore')


def load_data():
    df = pd.read_csv('retail_price.csv')

df = load_data()

def show_explore():
    df = pd.read_csv('retail_price.csv')
    st.title("Explore the Data")
    fig = px.scatter(df,
                     x='qty',
                     y='total_price', trendline='ols',
                     title='Quantity vs Total Price')
    st.pyplot(fig)


