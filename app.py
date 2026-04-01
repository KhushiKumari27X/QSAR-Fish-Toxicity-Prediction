import streamlit as st
import pandas as pd

st.title("QSAR Fish Toxicity Prediction")

st.write("Upload your dataset")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    data = pd.read_csv(file)
    st.write("Dataset Preview:")
    st.dataframe(data)

    st.write("Basic Info:")
    st.write(data.describe())