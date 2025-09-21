import streamlit as st
from pathlib import Path
from PIL import Image

# Page settings
st.set_page_config(page_title="📊 E-commerce Visualizations", layout="wide")

st.title("📊 E-commerce Visualizations from Notebook")
st.markdown("Visual insights generated from **main.ipynb** are displayed here in a structured dashboard.")

# Path to images folder
images_path = Path("ecs/images")

# Chart dictionary
plots = {
    "📈 Units Sold Over Time": ("plot1.png", "This chart shows how units sold fluctuate across time."),
    "💰 Price vs Units Sold": ("plot2.png", "Illustrates how product pricing affects sales volume."),
    "🎯 Discount Impact": ("plot3.png", "Highlights the role of discounts in driving higher sales."),
    "📦 Category Comparison": ("plot4.png", "Compares sales performance across different product categories.")
}

# Sidebar navigation
st.sidebar.header("🔍 Select Visualization")
selected_plot = st.sidebar.radio("Choose a chart to view:", list(plots.keys()))

# Display selected plot in a card
filename, insight = plots[selected_plot]
file_path = images_path / filename

if file_path.exists():
    col1, col2 = st.columns([2, 1])  # two-column layout
    with col1:
        image = Image.open(file_path)
        st.image(image, caption=selected_plot, use_container_width=True)

    with col2:
        with st.expander("📌 Key Insight", expanded=True):
            st.write(insight)
else:
    st.error(f" {filename} not found in {images_path}")

