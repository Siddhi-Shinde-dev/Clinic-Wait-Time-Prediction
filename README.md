Clinic Wait Time Prediction System
A Machine Learning-based system to forecast patient wait times in clinical settings. This project uses historical emergency room (ER) data to predict how long a patient will wait based on their visit details, urgency, and facility resources.

📋 Project Overview
This project processes medical data to predict Total Wait Time (min). It involves data cleaning, feature engineering (handling time-series data), and training various regression models to determine the most accurate wait time estimates.

📋 Key Features
Single Prediction: Input real-time visit details (Nurse-to-Patient ratio, Triage time, etc.) to get an instant wait time estimate.

Batch Prediction: Upload a CSV file to generate bulk wait time forecasts for multiple patients at once.

History Tracking: View a real-time log of predictions made during your current session, visualized with an interactive trend chart.

Data Export: Easily download your session's prediction history as a CSV file for reporting.

🛠️ Technologies Used
Python
Streamlit
Pandas
NumPy
Scikit-learn
Pickle

📊 Dataset Features
The model uses a dataset containing 5,000 patient records with the following key features:

Inputs: Nurse-to-Patient Ratio, Time to Registration (min), Time to Triage (min), Urgency Level, and dayofweek.

Target: Total Wait Time (min)

🤖 Models Trained
The project compares the performance of several regression models:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

K-Nearest Neighbors (KNN) Regressor

🚀 How to Run
Clone the repository:

Bash
git clone <your-repository-link>
cd Clinic-Wait-Time-Prediction
Install dependencies:

Bash
pip install -r requirements.txt
Launch the application:

Bash
streamlit run streamlit_app.py


📁 Project Structure

Clinic-Wait-Time-Prediction/

├── Dataset/               
│   └── clinic_dataset
│
├── notebooks/
│   └── ClinicWaitingTimeprediction.ipynb
│
├── screenshots/
│   └── batch_prediction_upload.pdf
│   └── dashboard_single_prediction.pdf
│   └── prediction_history_logs.pdf
│── app.py
├── .gitignore             
├── README.md            
├── requirements.txt       
├── streamlit_app.py        
└── wait_time_model.pkl     

