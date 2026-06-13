import mne
import numpy as np
import pandas as pd

# Load EEG data
file_path = "raw_data/EEG/S001/S001R01.edf"

raw = mne.io.read_raw_edf(
    file_path,
    preload=True
)

# Filter EEG
raw.filter(
    l_freq=1,
    h_freq=40
)

# Get signal matrix
data = raw.get_data()

# Feature extraction
mean_feature = np.mean(data)
std_feature = np.std(data)
rms_feature = np.sqrt(np.mean(data**2))
energy_feature = np.sum(data**2)
max_feature = np.max(data)
min_feature = np.min(data)

# Store features
features = {
    "mean": mean_feature,
    "std": std_feature,
    "rms": rms_feature,
    "energy": energy_feature,
    "max": max_feature,
    "min": min_feature
}

feature_df = pd.DataFrame([features])

# Save to CSV
feature_df.to_csv(
    "clean_data/eeg_features.csv",
    index=False
)

print("NeuroStrokeAI EEG Features Extracted Successfully\n")

print(feature_df)