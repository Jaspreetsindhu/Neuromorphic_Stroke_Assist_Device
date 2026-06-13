import os
import pandas as pd
import numpy as np
import mne

dataset = []

# ---------- EEG ----------
eeg_folder = "raw_data/EEG/S001"

for file in os.listdir(eeg_folder):

    if file.endswith(".edf"):

        path = os.path.join(eeg_folder, file)

        raw = mne.io.read_raw_edf(
            path,
            preload=True,
            verbose=False
        )

        raw.filter(
            l_freq=1,
            h_freq=40,
            verbose=False
        )

        data = raw.get_data()

        sample = {
            "EEG_mean": np.mean(data),
            "EEG_std": np.std(data),
            "EEG_rms": np.sqrt(np.mean(data**2)),
            "EEG_energy": np.sum(data**2)
        }

        dataset.append(sample)

# Save dataset
df = pd.DataFrame(dataset)

df.to_csv(
    "clean_data/eeg_dataset.csv",
    index=False
)

print(df.head())

print("\nEEG Dataset Created Successfully!")