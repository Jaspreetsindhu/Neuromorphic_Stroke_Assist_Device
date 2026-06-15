# 🧠 Neuromorphic Stroke Assist Devic

## 📌 Overview
The **Neuromorphic Stroke Assist Device** is an AI-based intelligent healthcare system designed for early detection and risk prediction of stroke. It uses machine learning techniques and data-driven analysis to evaluate patient health parameters and classify stroke risk levels in real time.

The system is designed as a **neuromorphic-inspired intelligent decision support system**, aiming to assist early diagnosis and improve emergency response efficiency.

---

## 🎯 Problem Statement
Stroke is one of the leading causes of death and long-term disability worldwide. Early detection significantly increases survival chances, but traditional diagnostic methods are slow and not suitable for real-time monitoring.

This project aims to:
- Detect stroke risk at an early stage using AI
- Enable fast and automated decision-making
- Support healthcare systems with real-time prediction

---

## ⚙️ Features
- 🧠 AI-based stroke risk prediction model  
- 📊 Data preprocessing and feature engineering  
- ⚡ Real-time prediction pipeline  
- 🚨 Risk classification (Low / Medium / High)  
- 📈 Performance evaluation using ML metrics  
- 🧾 Visual result analysis (graphs & confusion matrix)  

---

## 🧰 Tech Stack
- Python 🐍  
- NumPy  
- Pandas  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- TensorFlow / PyTorch *(if used)*  
- OpenCV *(if applicable)*  

---

## 📂 Dataset
- Dataset used: *(Add dataset name here, e.g., Kaggle Stroke Prediction Dataset)*  
- Type: Structured medical dataset  
- Features include: age, hypertension, heart disease, glucose level, BMI, etc.  

---

## 🏗️ System Architecture
The system follows a structured pipeline:

1. **Input Layer** → Patient health data collection  
2. **Preprocessing Layer** → Cleaning, normalization, feature extraction  
3. **Model Layer** → Machine learning model prediction  
4. **Decision Layer** → Risk classification (Low / Medium / High)  
5. **Output Layer** → Result display / alert generation  

---

## 🤖 Machine Learning Model
- Model Type: *(Random Forest / SVM / Neural Network — update this)*  
- Training Method: Supervised Learning  
- Output: Stroke risk classification  

---

## 📊 Accuracy and Metrics

The model was evaluated on the test dataset using standard classification metrics:

- **Processing Latency:** 8 ms  
- **Power Consumption:** 1.2 W  
- **Model Accuracy (Intent Detection):** 96%  
  
<img width="932" height="874" alt="image" src="https://github.com/user-attachments/assets/ecec9e62-f080-4b02-83ea-70269f9b8a09" />

---

## 📉 Confusion Matrix
The following confusion matrix shows the model’s performance in classifying stroke risk:

<img width="926" height="863" alt="image" src="https://github.com/user-attachments/assets/08a8080c-7a1d-4546-bf4b-bc7776e0e193" />

<img width="925" height="858" alt="image" src="https://github.com/user-attachments/assets/f6d3d412-bb98-45b5-87cb-8fc5de3ccd20" />

---

## 📈 Results
- High accuracy achieved in stroke risk classification  
- Effective real-time prediction system implemented  
- Model shows strong performance in identifying high-risk cases  
- Reliable decision support for early stroke detection  
<img width="889" height="831" alt="image" src="https://github.com/user-attachments/assets/a46781df-cc3e-434c-80a8-9777b45ee614" />

<img width="919" height="867" alt="image" src="https://github.com/user-attachments/assets/790f3af8-3369-4c04-ac27-6caa6adf6c5d" />

<img width="920" height="858" alt="image" src="https://github.com/user-attachments/assets/dbd1293c-f7c8-4c86-b9f8-b7bcb95210f9" />

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Jaspreetsindhu/Neuromorphic_Stroke_Assist_Device.git
```

### 2. Navigate to the Project Folder

```bash
cd Neuromorphic_Stroke_Assist_Device
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Navigate to the Dashboard Folder

```bash
cd NeuroStrokeAI
```

### 5. Launch the Application

```bash
streamlit run app.py
```

### 6. Open in Browser

Streamlit will generate a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your browser to access the NeuroStrokeAI dashboard.

## 📁 Project Structure

```
Neuromorphic_Stroke_Assist_Device/
│
├── src/                  # Source code modules
├── models/               # Trained ML models
├── dataset/              # Dataset files
├── docs/                 # Graphs & results (confusion matrix, etc.)
├── main.py               # Main execution file
├── requirements.txt      # Dependencies
└── README.md
```

---
## 🧠 Interpretation of Results

- ⚡ **8 ms latency** ensures real-time response suitable for assistive medical applications  
- 🔋 **1.2 W power consumption** indicates highly efficient system design for wearable/embedded use  
- 🎯 **96% accuracy** shows strong performance of the AI model in intent/stroke detection classification  

---
## 🚨 Assistive Device Behavior

When motor intent is detected by the model:

✔ System triggers assistive device activation  
✔ Provides real-time response output  
✔ Ensures fast decision-making for support systems  

---

## 📌 Summary

This system successfully combines:
- Machine Learning-based prediction  
- Real-time processing capability  
- Low-latency intelligent decision making  
- Efficient system-level performance metrics
  
## 🔮 Future Scope

* Integration with wearable IoT health sensors
* Mobile application for real-time monitoring
* Cloud-based patient tracking system
* Improved deep learning models for higher accuracy
* Edge AI / neuromorphic hardware implementation

---

## ⚠️ Disclaimer

This project is developed for **educational and research purposes only**. It should not be used as a replacement for professional medical diagnosis or treatment.

---

## 👨‍💻 Team

* Avani khare
* Jaspreet Sindhu
* Zigyasa Chaturvedi
