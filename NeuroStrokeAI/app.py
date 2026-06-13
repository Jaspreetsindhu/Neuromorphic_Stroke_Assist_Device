import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="NeuroStrokeAI",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 NeuroStrokeAI")
st.subheader("AI-Powered Stroke Prediction using EEG and EMG Features")

st.markdown("""
### About the Project
This system analyzes EEG and EMG signal features and predicts stroke risk using a trained Machine Learning model.

**Features:**
- EEG Feature Analysis
- EMG Feature Analysis
- Machine Learning Prediction
- Interactive Dashboard
""")

# Load Model
model = joblib.load("models/neurostroke_model.pkl")

# Load Dataset
df = pd.read_csv("clean_data/fused_dataset.csv")

st.markdown("---")

# Dataset Preview
st.header("📊 Dataset Preview")
st.dataframe(df.head())

# Prediction Button
if st.button("🚀 Run Prediction"):

    X = df.drop("label", axis=1)

    predictions = model.predict(X)

    result_df = df.copy()

    # Convert numeric prediction to readable label
    result_df["Prediction"] = [
        "Stroke Risk" if p == 1 else "Normal"
        for p in predictions
    ]

    stroke_count = sum(predictions)
    normal_count = len(predictions) - stroke_count

    st.success("✅ Prediction completed successfully!")

    # Metrics
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Stroke Risk Cases", stroke_count)

    with col2:
        st.metric("Normal Cases", normal_count)

    st.markdown("---")

    st.header("📋 Prediction Results")
    st.dataframe(result_df)

    # Download Results
    csv = result_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Results",
        data=csv,
        file_name="neurostroke_predictions.csv",
        mime="text/csv"
    )

st.markdown("---")
st.caption("NeuroStrokeAI | Hackathon Project")