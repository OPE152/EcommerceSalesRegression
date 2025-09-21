import streamlit as st

st.set_page_config(page_title="🏠 E-commerce Sales Dashboard", layout="wide")

st.title("🏠 Welcome to the E-commerce Sales Prediction App")

st.markdown("""
This application helps you:
- 📊 Explore sales data with interactive visualizations  
- 🔮 Predict sales (`Units Sold`) using advanced Machine Learning  
- 💡 Gain insights into how factors like **Price, Discount, Marketing Spend, and Customer Segments** impact sales.  

Use the sidebar to navigate between **Prediction** and **Visualization** pages.
""")

st.info("👈 Start by choosing a page from the sidebar.")