import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from utils import load_data, get_summary_statistics, plot_time_series, plot_correlation_matrix, plot_wind_analysis, plot_temperature_analysis, plot_histograms, plot_bubble_chart

# Page configuration
st.set_page_config(
    page_title="Solar Farm Data Dashboard",
    page_icon="🌞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the datasets
try:
    benin_df = load_data('benin-malanville.csv')
    sierraleone_df = load_data('sierraleone-bumbuna.csv')
    togo_df = load_data('togo-dapaong_qc.csv')
except FileNotFoundError as e:
    print(e)

# Add a sidebar
with st.sidebar:
    st.title('🌞 Solar Farm Data Dashboard')
    
    st.sidebar.title("Select Dataset")
    dataset = st.sidebar.selectbox("Choose a dataset", ["Benin", "Sierra Leone", "Togo"])

    if dataset == "Benin":
        df = benin_df
    elif dataset == "Sierra Leone":
        df = sierraleone_df
    else:
        df = togo_df

    year_list = list(df['Timestamp'].dt.year.unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = df[df['Timestamp'].dt.year == selected_year]

    # Update color themes with valid options
    color_theme_list = ['viridis', 'cividis', 'inferno', 'magma', 'plasma', 'turbo', 'sunset', 'sunsetdark', 'bluered', 'rdBu']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

# Plot and chart types
st.header(f"Solar Farm Data Analysis for {selected_year}")

# Summary Statistics
st.subheader("Summary Statistics")
st.write(get_summary_statistics(df_selected_year))

# Time Series Analysis
st.subheader("Time Series Analysis")
st.altair_chart(plot_time_series(df_selected_year, selected_color_theme), use_container_width=True)

# Correlation Analysis
st.subheader("Correlation Analysis")
st.altair_chart(plot_correlation_matrix(df_selected_year, selected_color_theme), use_container_width=True)

# Wind Analysis
st.subheader("Wind Analysis")
st.altair_chart(plot_wind_analysis(df_selected_year, selected_color_theme), use_container_width=True)

# Temperature Analysis
st.subheader("Temperature Analysis")
st.altair_chart(plot_temperature_analysis(df_selected_year, selected_color_theme), use_container_width=True)

# Histograms
# st.subheader("Distribution Analysis")
# st.plotly_chart(plot_histograms(df_selected_year, selected_color_theme), use_container_width=True)

# Bubble Chart
st.subheader("Complex Relationships")
st.plotly_chart(plot_bubble_chart(df_selected_year, selected_color_theme), use_container_width=True)

# Final step to make everything cohesive
st.write("Interactive and User-Friendly Dashboard for Solar Farm Data Analysis")
