import mne

file_path = "raw_data/EEG/S001/S001R01.edf"

raw = mne.io.read_raw_edf(
    file_path,
    preload=True
)

print("Original Data Loaded")

# Filter between 1 and 40 Hz
raw.filter(
    l_freq=1,
    h_freq=40
)

print("\nNeuroStrokeAI EEG Filtering Completed")

print(raw.info)