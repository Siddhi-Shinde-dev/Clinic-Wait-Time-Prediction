# 🏥 Clinic Wait Time Prediction System

A **Machine Learning-based web application** that predicts patient wait times in a clinic/ER setting based on staffing, triage, and visit data.

Built with **Streamlit** and **scikit-learn**, deployed on Streamlit Cloud.

---

## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://clinic-wait-time-prediction-xjfzgowdftdocnhkvyvnyp.streamlit.app/)

---

## 📌 Features

- 🔍 **Single Prediction** — Enter patient details and get instant wait time prediction
- 📁 **Batch Prediction** — Upload a CSV file and predict for multiple patients at once
- 📜 **Session History** — Track all predictions made during the session
- 📊 **Gauge Chart** — Visual indicator of wait time severity
- 💡 **Recommendations** — Actionable alerts based on predicted wait time

---

## 🧠 ML Model

| Algorithm | R² Score | MAE |
|---|---|---|
| **Linear Regression** ✅ | **0.954** | **10.21 min** |
| Random Forest | 0.952 | 10.62 min |
| KNN | 0.949 | 10.77 min |
| Decision Tree | 0.921 | 13.32 min |

> Linear Regression was selected as the best model with **95.4% accuracy** and lowest MAE.

---

## 📂 Project Structure

```
Clinic-Wait-Time-Prediction/
├── streamlit_app.py
├── .gitignore
├── requirements.txt
├── wait_time_model.pkl
├── notebooks/
│   └── ClinicWaitingTimeprediction.ipynb
├── Dataset/
│   └── clinic_dataset.csv
├── screenshots/
│   ├── dashboard_single_prediction.pdf
│   ├── batch_prediction_upload.pdf
│   └── prediction_history_logs.pdf
└── README.md
```

---

## ⚙️ Input Features

| Feature | Description |
|---|---|
| Nurse-to-Patient Ratio | Number of patients per nurse |
| Time to Registration (min) | Minutes taken for registration |
| Time to Triage (min) | Minutes taken for triage |
| Urgency Level | Low / Medium / High / Critical |
| Day of Week | Monday (0) to Sunday (6) |

**Target:** `Total Wait Time (min)`

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **ML:** scikit-learn, pandas, numpy
- **Visualization:** Plotly, Matplotlib
- **Model Persistence:** joblib
- **Deployment:** Streamlit Cloud

---

## 📦 Installation (Run Locally)

```bash
# Clone the repo
git clone https://github.com/Siddhi-Shinde-dev/Clinic-Wait-Time-Prediction
cd Clinic-Wait-Time-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

---

## 📊 Dataset

- **Source:** ER Wait Time Dataset (Kaggle)
- **Features:** 5 input features
- **Target:** Total Wait Time (min)
- **Train/Test Split:** 80/20

---

## 👩‍💻 Developer

**Siddhi Vinod Shinde**  

