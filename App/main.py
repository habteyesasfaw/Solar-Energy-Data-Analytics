import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Streamlit app title
st.title("Solar Energy Data Analysis")

# Dropdown menu to select dataset
dataset_option = st.selectbox(
    "Select a dataset to analyze",
    ["benin-malanville.csv", "sierraleone-bumbuna.csv", "togo-dapaong_qc.csv"]
)

# Define file paths (relative to the script directory)
dataset_paths = {
    "benin-malanville.csv": 'data/benin-malanville.csv',
    "sierraleone-bumbuna.csv": 'data/sierraleone-bumbuna.csv',
    "togo-dapaong_qc.csv": 'data/togo-dapaong_qc.csv'
}

# File uploader for user to upload the dataset
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Load dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    dataset_path = dataset_paths.get(dataset_option, '')
    if dataset_path:
        try:
            df = pd.read_csv(dataset_path)
        except FileNotFoundError:
            st.error(f"File not found: {dataset_path}")
            st.stop()

# Display dataset overview
st.write("### Dataset Overview")
st.write(df.head())
st.write("### Dataset Info")
st.write(df.info())
st.write("### Missing Values")
st.write(df.isnull().sum())

# Summary Statistics
st.write("### Summary Statistics")
st.write(df.describe())

# Data Quality Check
st.write("### Data Quality Check")
st.write("Missing values:")
st.write(df.isnull().sum())
st.write("Outliers and anomalies:")
for col in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']:
    st.write(f"{col}:")
    st.write(df[df[col] < 0].shape[0], "outliers")

# Time Series Analysis
st.write("### Time Series Analysis")
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)
st.line_chart(df[['GHI', 'DNI', 'DHI']])

# Correlation Analysis
st.write("### Correlation Analysis")
correlation_matrix = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
st.write("Correlation Matrix:")
st.write(correlation_matrix)
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Wind Analysis
st.write("### Wind Analysis")
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
wind_direction_rad = np.deg2rad(df['WD'].dropna())
wind_speed = df['WS'].dropna()
ax.scatter(wind_direction_rad, wind_speed, c='b', alpha=0.5)
ax.set_title("Wind Speed and Direction")
st.pyplot(fig)

# Temperature Analysis
st.write("### Temperature Analysis")
fig, ax = plt.subplots()
sns.scatterplot(x=df['RH'], y=df['Tamb'], ax=ax)
ax.set_xlabel("Relative Humidity (%)")
ax.set_ylabel("Ambient Temperature (°C)")
ax.set_title("RH vs Ambient Temperature")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.scatterplot(x=df['RH'], y=df['GHI'], ax=ax)
ax.set_xlabel("Relative Humidity (%)")
ax.set_ylabel("Global Horizontal Irradiance (W/m²)")
ax.set_title("RH vs GHI")
st.pyplot(fig)

# Histograms
st.write("### Histograms")
fig, ax = plt.subplots(2, 2, figsize=(12, 8))
sns.histplot(df['GHI'].dropna(), ax=ax[0, 0], bins=30, kde=True)
ax[0, 0].set_title('Histogram of GHI')

sns.histplot(df['DNI'].dropna(), ax=ax[0, 1], bins=30, kde=True)
ax[0, 1].set_title('Histogram of DNI')

sns.histplot(df['DHI'].dropna(), ax=ax[1, 0], bins=30, kde=True)
ax[1, 0].set_title('Histogram of DHI')

sns.histplot(df['WS'].dropna(), ax=ax[1, 1], bins=30, kde=True)
ax[1, 1].set_title('Histogram of Wind Speed')

st.pyplot(fig)

# Z-Score Analysis
st.write("### Z-Score Analysis")
z_scores = df[['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']].apply(zscore)
st.write("Z-Scores:")
st.write(z_scores)

# Bubble Charts
st.write("### Bubble Charts")
fig, ax = plt.subplots()
sns.scatterplot(
    x='GHI', y='Tamb', size='RH', sizes=(20, 200), hue='BP',
    data=df, ax=ax, palette='viridis', alpha=0.6, edgecolor=None
)
ax.set_xlabel("GHI (W/m²)")
ax.set_ylabel("Ambient Temperature (°C)")
ax.set_title("GHI vs Tamb with Bubble Size representing RH")
st.pyplot(fig)
