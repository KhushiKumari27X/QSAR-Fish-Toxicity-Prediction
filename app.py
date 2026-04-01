import streamlit as st
import pandas as pd
import numpy as np

st.title("QSAR Fish Toxicity Prediction")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    # Dummy prediction (replace with your model later)
    st.subheader("Prediction Results")

    df["Predicted Toxicity"] = np.random.choice(["Low", "Medium", "High"], size=len(df))

    st.write(df)

    # Download option
    st.download_button(
        label="Download Results",
        data=df.to_csv(index=False),
        file_name="prediction_results.csv",
        mime="text/csv"
    )