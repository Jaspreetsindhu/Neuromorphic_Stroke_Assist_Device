import numpy as np
from scipy import signal

def generate_and_filter_signal():
    fs = 250

    t = np.linspace(0, 5, fs * 5)

    eeg_signal = np.sin(2 * np.pi * 10 * t)

    noise = np.random.normal(0, 0.5, len(t))

    noisy_signal = eeg_signal + noise

    b, a = signal.butter(4, 30/(fs/2), btype='low')

    filtered_signal = signal.filtfilt(b, a, noisy_signal)

    return filtered_signal