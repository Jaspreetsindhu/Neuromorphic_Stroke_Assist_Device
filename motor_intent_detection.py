import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Simulated EEG features
X = np.array([
    [0.1, 0.5, 1.0, -1.0],
    [0.2, 0.6, 1.1, -0.9],
    [0.8, 1.2, 2.0, -2.0],
    [0.9, 1.3, 2.1, -2.1],
    [0.15, 0.55, 1.05, -1.05],
    [0.85, 1.25, 2.05, -2.05]
])

# Labels
# 0 = No movement
# 1 = Movement intent
y = np.array([0, 0, 1, 1, 0, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

result_text = f"Model Accuracy: {accuracy}\n"

new_signal = [[0.88, 1.28, 2.08, -2.08]]
prediction = model.predict(new_signal)

if prediction[0] == 1:
    result_text += "Motor Intent Detected"
else:
    result_text += "No Motor Intent Detected"

print(result_text)

with open("results/model_results.txt", "w") as file:
    file.write(result_text)

# Test a new signal
new_signal = [[0.88, 1.28, 2.08, -2.08]]

prediction = model.predict(new_signal)

