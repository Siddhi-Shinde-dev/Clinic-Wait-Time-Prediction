# 🏥 Clinic Wait Time Prediction System

A **Machine Learning-based system** to forecast patient waiting time in clinical settings.
This project uses historical Emergency Room (ER) data to predict how long a patient will wait based on visit details, urgency level, and facility resources.

---

## 📌 Project Overview

The system processes healthcare data to predict **Total Wait Time (minutes)**.

It includes:

* Data cleaning and preprocessing
* Feature engineering for time-based data
* Training and comparison of multiple regression models
* Real-time wait time prediction through an interactive Streamlit dashboard

---

## ✨ Key Features

### 🔹 Single Prediction

Enter patient visit details and get an instant wait time estimate.

Inputs include:

* Nurse-to-Patient Ratio
* Registration Time
* Triage Time
* Urgency Level
* Day of Week

---

### 🔹 Batch Prediction

Upload a CSV file containing multiple patient records and generate predictions for all patients at once.

---

### 🔹 Prediction History Tracking

* Stores prediction records during the current session
* Displays wait-time trends using interactive charts
* Helps analyze prediction patterns

---

### 🔹 Data Export

Download prediction history as a CSV file for reporting and analysis.

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Pickle

---

# 📊 Dataset Description

The dataset contains **5,000 patient records**.

### Features

| Feature                | Description                       |
| ---------------------- | --------------------------------- |
| Nurse-to-Patient Ratio | Available nursing resources       |
| Registration Time      | Time taken for registration       |
| Triage Time            | Time taken for patient assessment |
| Urgency Level          | Patient priority level            |
| Day of Week            | Visit day information             |

### Target Variable

**Total Wait Time (minutes)**

---

# 🤖 Machine Learning Models

The following regression models were trained and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* K-Nearest Neighbors (KNN) Regressor

The best-performing model was selected and saved for deployment.

---

# 🚀 How to Run

## 1. Clone Repository

```bash
git clone <https://github.com/Siddhi-Shinde-dev/Clinic-Wait-Time-Prediction>

cd Clinic-Wait-Time-Prediction
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Application

```bash
streamlit run streamlit_app.py
```

---

# 📁 Project Structure

```
Clinic-Wait-Time-Prediction/

│
├── Dataset/
│   └── clinic_dataset.csv
│
├── notebooks/
│   └── ClinicWaitingTimePrediction.ipynb
│
├── screenshots/
│   ├── batch_prediction_upload.pdf
│   ├── dashboard_single_prediction.pdf
│   └── prediction_history_logs.pdf
│
├── app.py
├── streamlit_app.py
├── wait_time_model.pkl
├── requirements.txt
├── README.md
└── .gitignore

---

## 📷 Screenshots

### Dashboard - Single Prediction

[View Dashboard Screenshot](screenshots/dashboard_single_prediction.pdf)

### Batch Prediction

[View Batch Prediction Screenshot](screenshots/batch_prediction_upload.pdf)

### Prediction History

[View Prediction Logs](screenshots/prediction_history_logs.pdf)

---

# 🎯 Future Improvements

* Deploy the application online
* Add real-time hospital queue integration
* Improve accuracy with advanced ML models
* Add patient priority recommendation system

---

# 👩‍💻 Author

**Siddhi Vinod Shinde**
