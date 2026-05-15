import streamlit as st
import pandas as pd
import numpy as np

# title of the application
st.title("Real Time Anomaly Detection Engine")

# create a simple text
st.write("This is the learning method used for streamlit")

# # create a simple Dataframe
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

# # display the dataframe
# st.write("Here is the dataframe")
# st.write(df)

# # create a line chart
# chart_data = pd.DataFrame(
#     np.random.randn(20,3),
#     columns= ['a','b','c']
# )
# st.line_chart(chart_data)

name = st.text_input("Enter your name: ")

age = st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}")

options = ["python","java","C++","JavaScript"]
choice = st.selectbox("Choose your favorite language: ", options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello, {name}")


data = {
    "Name": ["John","Jane","Jake","Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York","Los Angeles","Chicago","Houston"]
}

df= pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

uploaded_file = st.file_uploader("choose a CSV file", type= "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

