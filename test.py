import streamlit as st
import pandas as pd

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

# Set 'category' as index
df.set_index('category', inplace=True)

# Display the DataFrame in Streamlit
st.write("Displaying the DataFrame:")
st.write(df)

# Plotting a bar chart
st.write("Bar chart based on the data:")
st.bar_chart(df)
