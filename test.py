import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

# Sample data (Replace this with your actual data)
data = {
    'School': ['School1', 'School2', 'School3', 'School4', 'School5'],
    'Name2': [115, 202, 206, 683, 37],
    'Name3': [378, 131, 956, 183, 541],
    'Name4': [439, 35, 635, 861, 510],
    'Name5': [274, 156, 990, 39, 664]
}

df = pd.DataFrame(data)
df.set_index('School', inplace=True)

# Display the DataFrame
st.write("## DataFrame")
st.write(df)

