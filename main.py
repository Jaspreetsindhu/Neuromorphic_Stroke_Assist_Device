from signal_processing import generate_and_filter_signal
from feature_extraction import extract_features
from motor_intent_detection import predict_motor_intent

print("Neuromorphic Stroke Rehabilitation System Started")

signal_data = generate_and_filter_signal()

features = extract_features(signal_data)

prediction = predict_motor_intent(features)

if prediction == 1:
    result = "Motor Intent Detected"
else:
    result = "No Motor Intent Detected"

print(result)

with open("results/model_results.txt", "w") as file:
    file.write(result)