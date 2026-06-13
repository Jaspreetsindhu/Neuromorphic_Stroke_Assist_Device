import os
import pandas as pd
import numpy as np

dataset = []

base_folder = "raw_data/EMG"

subjects = ["sub", "sub1", "sub2", "sub3", "sub4"]

for subject in subjects:

    aggressive_folder = os.path.join(
        base_folder,
        subject,
        "Aggressive"
    )

    for file in os.listdir(aggressive_folder):

        if file.endswith(".csv"):

            path = os.path.join(
                aggressive_folder,
                file
            )

            df = pd.read_csv(path)

            signals = df.drop(
                columns=["label"]
            )

            sample = {

                "EMG_mean":
                    signals.mean().mean(),

                "EMG_std":
                    signals.std().mean(),

                "EMG_rms":
                    np.sqrt(
                        np.mean(
                            signals**2
                        )
                    ).mean(),

                "EMG_energy":
                    np.sum(
                        signals.values**2
                    )
            }

            dataset.append(sample)

emg_df = pd.DataFrame(dataset)

emg_df.to_csv(
    "clean_data/emg_dataset.csv",
    index=False
)

print(emg_df.head())

print("\nEMG Dataset Created Successfully!")