import streamlit as st
import pickle

def load_model():
    with open('model1.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

def predict_page():
    st.title("Price Optimization")
    st.write("""#### we need some info""")

    cate = ('bed_bath_table', 'garden_tools', 'consoles_games',
       'health_beauty', 'cool_stuff', 'perfumery',
       'computers_accessories', 'watches_gifts', 'furniture_decor')

    category = st.selectbox("Category",cate)
    total_price = st.number_input("Enter total_price", min_value=0, max_value=15000, value=1500, step=1)
    shipping = st.number_input("Enter shipping price", min_value=0, max_value=100, value=50, step=1)
    customer_price = st.number_input("Enter number of Customers", min_value=0, max_value=500, value=50, step=1)
    product_score = st.number_input("Enter product score(rating)",min_value=0.0, max_value=5.0,value=3.0,step=1.0,format="%.2f")

    OK = st.button("Calculate unit price")

    if OK:
        X = [[total_price,shipping,customer_price,product_score]]

        price = data.predict(X)
        st.subheader(f"The estimated unit price ${price}")

