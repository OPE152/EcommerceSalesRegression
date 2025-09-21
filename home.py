import streamlit as st

st.set_page_config(page_title="E-commerce Sales App", layout="wide")

st.title("🏠 Welcome to the E-commerce Sales Prediction App")

st.write(
    """
    This app helps businesses **predict product sales** and 
    **analyze important trends** using machine learning.  

    🔍 **What you can do here:**
    - Go to the **Predictions Page** to forecast sales.
    - Explore **Visualizations** to uncover trends in pricing, discounts, and marketing spend.
    """
)

st.markdown("### 📂 Pages in this App")
st.markdown("- 🏠 **Home** → Overview of the project")  
st.markdown("- 🔮 **Predictions** → Predict future sales")  
st.markdown("- 📊 **Visualization** → Explore insights and trends")  

st.success("👉 Use the sidebar to navigate between pages.")