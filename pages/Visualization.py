import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualizations", page_icon="📊")

st.title("📊 Sales Visualization Page")

st.write("Explore trends and insights from the dataset.")

# Load dataset
df = pd.read_csv("C:\Users\HP\Documents\Project\deployed_app\ecs\data\ecommerce_output.csv")

# --- Plot 1: Distribution of Sales ---
st.subheader("Distribution of Units Sold")
fig, ax = plt.subplots()
sns.histplot(df["Units_Sold"], bins=30, kde=True, ax=ax)
st.pyplot(fig)
st.caption("Units Sold follow a skewed distribution, with most sales clustering in lower ranges.")

# --- Plot 2: Price vs Units Sold ---
st.subheader("Price vs Units Sold")
fig, ax = plt.subplots()
sns.scatterplot(x="Price", y="Units_Sold", data=df, hue="Discount", palette="coolwarm", ax=ax)
st.pyplot(fig)
st.caption("Higher prices generally reduce sales, while higher discounts boost sales.")

# --- Plot 3: Marketing Spend Impact ---
st.subheader("Marketing Spend vs Units Sold")
fig, ax = plt.subplots()
sns.lineplot(x="Marketing_Spend", y="Units_Sold", data=df, ax=ax)
st.pyplot(fig)
st.caption("Sales tend to increase as marketing spend rises.")