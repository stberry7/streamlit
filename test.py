import streamlit as st
import pandas as pd

# URL of the raw CSV file in your GitHub repository
url = "https://raw.githubusercontent.com/stberry7/streamlit/main/school.csv"

# Read the CSV file directly in your Streamlit app
df = pd.read_csv(url)

# Display the DataFrame in Streamlit
st.write("Displaying the DataFrame:")
st.write(df)

# Plotting a bar chart
st.write("Bar chart based on Total Students in each School:")
st.bar_chart(df.set_index('School_Name')['Total_Students'])
