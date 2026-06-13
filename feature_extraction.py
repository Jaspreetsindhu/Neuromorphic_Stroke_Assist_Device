import numpy as np

# Create sample EEG signal
fs = 250
t = np.linspace(0, 5, fs * 5)

eeg_signal = np.sin(2 * np.pi * 10 * t)

# Feature 1: Mean
mean_value = np.mean(eeg_signal)

# Feature 2: Standard Deviation
std_value = np.std(eeg_signal)

# Feature 3: Maximum Value
max_value = np.max(eeg_signal)

# Feature 4: Minimum Value
min_value = np.min(eeg_signal)

print("Mean:", mean_value)
print("Standard Deviation:", std_value)
print("Maximum:", max_value)
print("Minimum:", min_value)