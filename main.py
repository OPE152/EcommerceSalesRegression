import streamlit as st

st.set_page_config(page_title="About Project", layout="wide")

st.title("ℹ️ About This Project")

st.write(
    """
    This project is designed to **predict e-commerce product sales** using 
    historical data and **machine learning techniques**.  

    The app has four key sections:
    - 🏠 **Home** → Introduction & navigation
    - 🔮 **Predictions** → Forecast future sales based on input features
    - 📊 **Visualization** → Explore dataset trends and patterns
    - ℹ️ **About** → Learn about the project objective, dataset, and ML model
    """
)

st.markdown("---")

## 🎯 Project Objective
st.header("🎯 Project Objective")
st.write(
    """
    The main goal of this project is to help e-commerce businesses:
    - Predict **Units Sold** for different products
    - Optimize **pricing, discounting, and marketing spend**
    - Identify patterns in sales behavior over time
    """
)

## 📂 Dataset
st.header("📂 Dataset")
st.write(
    """
    The dataset used here contains:
    - Product details (Price, Discount, Category)
    - Customer information (Segment)
    - Marketing spend
    - Time-based features (Year, Month, Day, Weekend flag)
    - Target variable: **Units Sold**

    This dataset was cleaned and preprocessed before model training.
    """
)

## 🤖 Machine Learning Pipeline
st.header("🤖 Machine Learning Pipeline")
st.write(
    """
    The machine learning pipeline includes:
    - **Preprocessing**: Handling categorical features, scaling numerical values
    - **Feature Engineering**: Adding `IsWeekend`, extracting temporal features
    - **Model Training**: Random Forest Regressor (best performing model)
    - **Evaluation**: Metrics like R² and RMSE were used for performance tracking
    """
)

st.info("The best-performing model achieved strong accuracy, making it suitable for real-world decision support.")

st.markdown("---")

st.success("✅ This project demonstrates the end-to-end process of data cleaning, EDA, feature engineering, ML modeling, and deployment using Streamlit.")