#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import plotly.express as px


# In[2]:


# Set Streamlit page title
st.set_page_config(page_title="Sunspot Prediction Dashboard", layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv")
    
    # Clean column names (remove extra spaces)
    df.columns = df.columns.str.strip()
    
    # Ensure the date column is correctly parsed
    if "Month" not in df.columns:
        st.error("❌ Error: 'Month' column not found in dataset!")
        return None
    
    df["Month"] = pd.to_datetime(df["Month"])
    df.set_index("Month", inplace=True)
    df = df.asfreq('MS')  # Ensure monthly frequency

    # Check for correct sunspot column
    if "Avg_sunspot_count" in df.columns:
        df["Avg_sunspot_count"].fillna(method="ffill", inplace=True)  # Forward-fill missing values
    else:
        st.error("❌ Error: 'Avg_sunspot_count' column not found! Check CSV column names.")
        return None
    
    return df

# Load data
df = load_data()

if df is not None:
    # Sidebar controls
    st.sidebar.header("⚙️ Settings")
    n_months = st.sidebar.slider("📆 Months to Forecast", 1, 24, 12)  # User selects forecast period

    # 🔮 Predict button
    predict_button = st.sidebar.button("🔮 Predict")

    # Display dataset preview
    st.subheader("📊 Sunspot Data Overview")
    st.dataframe(df.tail(10))

    # Plot historical sunspot trends
    st.subheader("📈 Historical Sunspot Trends")
    fig = px.line(df, x=df.index, y=df["Avg_sunspot_count"], title="Sunspot Count Over Time")
    st.plotly_chart(fig)

    # Forecast only when user clicks "Predict"
    if predict_button:
        st.subheader("🔮 Future Sunspot Predictions")
        
        # Train ARIMA model
        model = ARIMA(df["Avg_sunspot_count"], order=(5,1,0))  # Adjust ARIMA order as needed
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=n_months)

        # Create forecast DataFrame
        future_dates = pd.date_range(start=df.index[-1], periods=n_months+1, freq='MS')[1:]
        forecast_df = pd.DataFrame({"Month": future_dates, "Predicted Sunspots": forecast})
        forecast_df.set_index("Month", inplace=True)

        # Show forecast data
        st.dataframe(forecast_df)

        # Plot forecasted values
        fig_forecast = px.line(forecast_df, x=forecast_df.index, y="Predicted Sunspots", title="Predicted Sunspot Counts")
        st.plotly_chart(fig_forecast)

        # Option to download forecast
        st.sidebar.download_button(
            label="📥 Download Forecast",
            data=forecast_df.to_csv(),
            file_name="sunspot_forecast.csv",
            mime="text/csv"
        )

        st.success("🌞 Prediction Complete!")
else:
    st.error("⚠️ Unable to load dataset. Please check the file format and column names.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




