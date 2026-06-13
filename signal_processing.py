import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Create a sample EEG signal
fs = 250  # Sampling frequency

t = np.linspace(0, 5, fs * 5)

eeg_signal = np.sin(2 * np.pi * 10 * t)

# Add noise
noise = np.random.normal(0, 0.5, len(t))
noisy_signal = eeg_signal + noise

# Create low-pass filter
b, a = signal.butter(4, 30/(fs/2), btype='low')

filtered_signal = signal.filtfilt(b, a, noisy_signal)

# Plot signals
plt.figure(figsize=(10,5))

plt.plot(t, noisy_signal, label="Noisy EEG")
plt.plot(t, filtered_signal, label="Filtered EEG")

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("EEG Signal Filtering")
plt.legend()

plt.savefig("results/eeg_filtering_result.png", dpi=300, bbox_inches="tight")
plt.show()