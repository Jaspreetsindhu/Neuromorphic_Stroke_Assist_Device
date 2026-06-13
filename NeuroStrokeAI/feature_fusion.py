import pandas as pd

# Load feature files
eeg_df = pd.read_csv("clean_data/eeg_features.csv")
emg_df = pd.read_csv("clean_data/emg_features.csv")

# Rename columns
eeg_df = eeg_df.add_prefix("EEG_")
emg_df = emg_df.add_prefix("EMG_")

# Combine horizontally
fusion_df = pd.concat([eeg_df, emg_df], axis=1)

# Save fused features
fusion_df.to_csv(
    "clean_data/fused_features.csv",
    index=False
)

print("EEG + EMG Fusion Completed Successfully!\n")
print(fusion_df)