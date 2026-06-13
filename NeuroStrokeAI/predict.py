import pandas as pd
import joblib

# Load model
model = joblib.load("models/neurostroke_model.pkl")

# Load one sample
df = pd.read_csv("clean_data/fused_dataset.csv")

# Remove label column
X = df.drop("label", axis=1)

# Predict
prediction = model.predict(X)

print("Predictions:")
print(prediction)