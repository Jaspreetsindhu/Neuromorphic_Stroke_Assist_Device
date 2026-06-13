import pandas as pd

# Load datasets
eeg_df = pd.read_csv("clean_data/eeg_dataset.csv")
emg_df = pd.read_csv("clean_data/emg_dataset.csv")

# Equalize lengths
n = min(len(eeg_df), len(emg_df))

eeg_df = eeg_df.iloc[:n]
emg_df = emg_df.iloc[:n]

# Combine
fused_df = pd.concat(
    [eeg_df.reset_index(drop=True),
     emg_df.reset_index(drop=True)],
    axis=1
)

# Create dummy labels
labels = []

for i in range(n):

    if i % 3 == 0:
        labels.append(0)

    elif i % 3 == 1:
        labels.append(1)

    else:
        labels.append(2)

fused_df["label"] = labels

# Save
fused_df.to_csv(
    "clean_data/fused_dataset.csv",
    index=False
)

print(fused_df.head())

print("\nFused Dataset Created Successfully!")