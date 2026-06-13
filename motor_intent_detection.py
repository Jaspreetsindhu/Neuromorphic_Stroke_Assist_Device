import numpy as np
from sklearn.ensemble import RandomForestClassifier

def predict_motor_intent(features):

    X = np.array([
        [0.1, 0.5, 1.0, -1.0],
        [0.2, 0.6, 1.1, -0.9],
        [0.8, 1.2, 2.0, -2.0],
        [0.9, 1.3, 2.1, -2.1],
        [0.15, 0.55, 1.05, -1.05],
        [0.85, 1.25, 2.05, -2.05]
    ])

    y = np.array([0, 0, 1, 1, 0, 1])

    model = RandomForestClassifier()

    model.fit(X, y)

    prediction = model.predict([features])

    return prediction[0]