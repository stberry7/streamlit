import streamlit as st
import pandas as pd

# URL of the raw CSV file in your GitHub repository
url = "https://raw.githubusercontent.com/stberry7/streamlit/main/school.csv"

# Read the CSV file directly in your Streamlit app
df = pd.read_csv(url)

# Display the DataFrame in Streamlit
st.write("Displaying the DataFrame:")
st.write(df)

# Check if the required columns exist in the DataFrame
if 'School_Name' in df.columns and 'Total_Students' in df.columns:
    # Plotting a bar chart
    st.write("Bar chart based on Total Students in each School:")
    chart_data = df[['School_Name', 'Total_Students']].set_index('School_Name')
    st.bar_chart(chart_data)
else:
    st.write("Could not find the required columns for plotting the bar chart.")
