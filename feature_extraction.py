import numpy as np

def extract_features(signal_data):

    mean_value = np.mean(signal_data)

    std_value = np.std(signal_data)

    max_value = np.max(signal_data)

    min_value = np.min(signal_data)

    features = [
        mean_value,
        std_value,
        max_value,
        min_value
    ]

    return features