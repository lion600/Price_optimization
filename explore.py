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
    fig1 = px.scatter(df,
                     x='qty',
                     y='total_price', trendline='ols',
                     title='Quantity vs Total Price')
    st.plotly_chart(fig1)

    fig2 = px.bar(df, x='product_category_name',
                 y='total_price', title='Total Price by Product Category')
    st.plotly_chart(fig2)

    fig3 = px.box(df, x='weekday',
                 y='total_price',
                 title='Box Plot of Total Price by number of Weekdays in a Month')
    st.plotly_chart(fig3)

    df['comp1_diff'] = df['unit_price'] - df['comp_1']
    df['comp2_diff'] = df['unit_price'] - df['comp_2']
    df['comp3_diff'] = df['unit_price'] - df['comp_3']

    for i in range(1, 4):
        comp = f"comp{i}_diff"
        fig4 = px.bar(x=df['product_category_name'],
                     y=df[comp],
                     title=f"Competitor {i} Price Difference per Unit",
                     labels={
                         'x': 'Product Category',
                         'y': f'Competitor {i}'
                     })
        st.plotly_chart(fig4)
    monthly_df = df.groupby(by='month_year').agg({
        'unit_price': 'mean', 'total_price': 'sum', 'freight_price': 'sum',
        'qty': 'sum', 'weekday': 'sum', 'weekend': 'sum', 'customers': 'sum'
    }).reset_index()
    monthly_df['month_year'] = pd.to_datetime(monthly_df['month_year'], format='%d-%m-%Y')
    monthly_df = monthly_df.sort_values(by='month_year')
    fig5 = px.scatter(monthly_df,
                     x='customers', y='total_price', trendline='ols',
                     title='Total Price vs Number of Customers')
    st.plotly_chart(fig5)


