import pandas as pd

# Path to one EMG file
file_path = "raw_data/EMG/sub/Aggressive/Punching.csv"

# Load data
df = pd.read_csv(file_path)

print("NeuroStrokeAI EMG Dataset Loaded Successfully")
print()

# Show first 5 rows
print(df.head())