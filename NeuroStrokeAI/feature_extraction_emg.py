import pandas as pd
import numpy as np

file_path = "raw_data/EMG/sub/Aggressive/Punching.csv"

df = pd.read_csv(file_path)

signals = df.drop(columns=["label"])

features = {
    "mean": signals.mean().mean(),
    "std": signals.std().mean(),
    "rms": np.sqrt(np.mean(signals**2)).mean(),
    "max": signals.max().max(),
    "min": signals.min().min()
}

feature_df = pd.DataFrame([features])

feature_df.to_csv(
    "clean_data/emg_features.csv",
    index=False
)

print("Features saved successfully!")
print(feature_df)