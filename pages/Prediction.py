import streamlit as st
import pandas as pd
import joblib

# Load model
import os, joblib

BASE_DIR = os.path.dirname(__file__)  # points to "deployed_app/pages"
model_path = os.path.join(BASE_DIR, "..", "ecs", "ecom_best_pipeline.pkl")
model_path = os.path.abspath(model_path)  # makes it a full path

model = joblib.load(model_path)

st.title("📊 E-commerce Sales Prediction")

# Inputs
price = st.number_input("Price", min_value=0.0)
discount = st.number_input("Discount", min_value=0.0, max_value=1.0, step=0.05)
marketing = st.number_input("Marketing Spend", min_value=0.0)
year = st.number_input("Year", min_value=2020, max_value=2030, step=1)
month = st.selectbox("Month", list(range(1,13)))
day = st.selectbox("Day", list(range(1,32)))
product_category = st.selectbox("Product Category", ["Electronics","Clothing","Furniture"])
customer_segment = st.selectbox("Customer Segment", ["Occasional","Regular","Premium"])

if st.button("Predict Sales"):
    input_df = pd.DataFrame([[price, discount, marketing, year, month, day, product_category, customer_segment]],
                            columns=['Price','Discount','Marketing_Spend','Year','Month','Day','Product_Category','Customer_Segment'])
    pred = model.predict(input_df)[0]
    st.success(f"✅ Predicted Units Sold: {pred:.0f}")