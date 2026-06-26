import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Clinic Wait Time Prediction",
    page_icon="🏥",
    layout="wide"
)

# ---------------- MODEL LOADING ----------------
@st.cache_resource
def load_model():
    # Ensure your 'wait_time_model.pkl' is in the root of your GitHub repo
    return joblib.load('wait_time_model.pkl')

model = load_model()

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    div[data-testid="stMetric"] { background: linear-gradient(135deg, #f0f8ff 0%, #e6f2fb 100%); border: 1px solid #cfe6f5; border-radius: 12px; padding: 16px 12px; }
    div[data-testid="stMetric"] label { color: #0E76A8 !important; font-weight: 600; }
    .stButton > button { border-radius: 10px; font-weight: 600; }
    .stButton > button[kind="primary"] { background-color: #0E76A8; border: none; }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- UI ----------------
st.markdown("<h1 style='text-align:center;'>🏥 Clinic Wait Time Prediction System</h1>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["🔍 Single Prediction", "📁 Batch Prediction (CSV)", "📜 History"])

# --- TAB 1: SINGLE PREDICTION ---
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        nurse_ratio = st.number_input("Nurse-to-Patient Ratio", min_value=1, value=3)
        reg_time = st.number_input("Time to Registration (min)", min_value=0.0, value=10.0)
    with col2:
        triage_time = st.number_input("Time to Triage (min)", min_value=0.0, value=15.0)
        urgency = st.selectbox("Urgency Level", ["Low", "Medium", "High", "Critical"])
        day_of_week = st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    day_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

    if st.button("🔍 Predict Wait Time", type="primary"):
        input_data = pd.DataFrame({
            "Nurse-to-Patient Ratio": [nurse_ratio],
            "Time to Registration (min)": [reg_time],
            "Time to Triage (min)": [triage_time],
            "Urgency Level": [urgency],
            "dayofweek": [day_map[day_of_week]]
        })
        
        try:
            prediction = model.predict(input_data)
            wait_time = float(prediction[0])
            st.metric("⏱ Predicted Wait Time", f"{wait_time:.1f} min")
            st.session_state.history.append({"Time": datetime.now().strftime("%H:%M:%S"), "Predicted": round(wait_time, 1)})
        except Exception as e:
            st.error(f"⚠ Prediction error: {e}")

# --- TAB 2 & 3: (Keep your Batch and History logic here, just ensure no requests.post is used) ---
# Note: For Batch, use the same 'model.predict(df)' method instead of calling an API.