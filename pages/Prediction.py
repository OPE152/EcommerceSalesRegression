import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Predictions", page_icon="🔮")

# Load model
pipe = joblib.load("ecom_best_pipeline.pkl")

st.title("🔮 Sales Prediction Page")

st.write("Enter product and marketing details to predict **Units Sold**.")

# --- Input form ---
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        price = st.number_input("Price", value=500.0)
        discount = st.slider("Discount (%)", 0, 50, 10)
        marketing_spend = st.number_input("Marketing Spend", value=1000.0)
    with col2:
        year = st.number_input("Year", value=2023, min_value=2000, max_value=2030)
        month = st.selectbox("Month", list(range(1,13)))
        day = st.number_input("Day", value=1, min_value=1, max_value=31)
        prod_cat = st.text_input("Product Category", "Electronics")
        cust_seg = st.text_input("Customer Segment", "Retail")

    submitted = st.form_submit_button("🚀 Predict")

if submitted:
    input_df = pd.DataFrame([{
        'Price': price, 'Discount': discount, 'Marketing_Spend': marketing_spend,
        'Year': year, 'Month': month, 'Day': day, 'IsWeekend': 1 if day%7 in (6,0) else 0,
        'Product_Category': prod_cat, 'Customer_Segment': cust_seg
    }])

    pred = pipe.predict(input_df)[0]
    st.success(f"Predicted Units Sold: **{pred:.0f}**")