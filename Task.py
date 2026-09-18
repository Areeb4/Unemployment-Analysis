import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Unemployment Analysis Dashboard", layout="wide")

st.title("📊 Unemployment Analysis Dashboard")
st.markdown("Exploring unemployment trends, rates, and distributions using Python and Streamlit.")

# Safe file loading path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Unemployment in India.csv')

@st.cache_data
def load_data():
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
    
    # Toggle to show raw dataset
    if st.checkbox("Show Raw Dataset"):
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

    # Summary statistics
    st.subheader("Dataset Summary Statistics")
    st.write(df.describe())

    # Visualizations layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Unemployment Rate Distribution")
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.histplot(df['Estimated Unemployment Rate (%)'], kde=True, ax=ax, color='blue')
        st.pyplot(fig)

    with col2:
        st.subheader("Unemployment Rate by Region")
        fig2, ax2 = plt.subplots(figsize=(7, 5))
        sns.barplot(data=df, x='Estimated Unemployment Rate (%)', y='Region', ax=ax2, palette='viridis')
        st.pyplot(fig2)

except Exception as e:
    st.error(f"Error loading data: {e}")