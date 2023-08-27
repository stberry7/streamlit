import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

# Sample data as a dictionary (Replace this with your CSV read)
data = {
    'category': ['School1', 'School2', 'School3', 'School4', 'School5', 'School6', 'School7', 'School8', 'School9', 'School10', 'School11'],
    'Name2': [115, 202, 206, 683, 37, 796, 56, 551, 578, 904, 446],
    'Name3': [378, 131, 956, 183, 541, 155, 903, 688, 573, 491, 394],
    'Name4': [439, 35, 635, 861, 510, 540, 864, 632, 609, 391, 139],
    'Name5': [274, 156, 990, 39, 664, 479, 405, 763, 53, 643, 361]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)
df.set_index('category', inplace=True)

# Display DataFrame
st.write("## Displaying the DataFrame:")
st.write(df)

# Matplotlib Charts
st.write("## Matplotlib Charts")

# Bar Chart
st.write("### Bar Chart")
plt.figure(figsize=[10,5])
df.plot(kind='bar')
plt.title('Matplotlib Bar Chart')
plt.ylabel('Value')
plt.xlabel('Category')
st.pyplot()

# Line Chart
st.write("### Line Chart")
plt.figure(figsize=[10,5])
df.plot(kind='line')
plt.title('Matplotlib Line Chart')
plt.ylabel('Value')
plt.xlabel('Category')
st.pyplot()

# Plotly Charts
st.write("## Plotly Charts")

# Bar Chart
st.write("### Bar Chart")
fig = px.bar(df, x=df.index, title="Plotly Bar Chart")
st.plotly_chart(fig)

# Line Chart
st.write("### Line Chart")
fig = px.line(df, x=df.index, title="Plotly Line Chart")
st.plotly_chart(fig)

# Altair Charts
st.write("## Altair Charts")

# Bar Chart
st.write("### Bar Chart")
chart = alt.Chart(df.reset_index()).mark_bar().encode(
    x='category',
    y='Name2',
    color='category'
).properties(
    title='Altair Bar Chart'
)
st.altair_chart(chart, use_container_width=True)

# Line Chart
st.write("### Line Chart")
chart = alt.Chart(df.reset_index()).mark_line().encode(
    x='category',
    y='Name2',
    color='category'
).properties(
    title='Altair Line Chart'
)
st.altair_chart(chart, use_container_width=True)

