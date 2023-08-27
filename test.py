import streamlit as st
import pandas as pd

# URL of the raw CSV file in your GitHub repository
url = "https://raw.githubusercontent.com/stberry7/streamlit/main/school.csv"

# Read the CSV file directly in your Streamlit app
df = pd.read_csv(url)

# Display the DataFrame in Streamlit
st.write(df)
