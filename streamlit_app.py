import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Clinic Wait Time Prediction",
    page_icon="🏥",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    /* Overall page padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f2fb 100%);
        border: 1px solid #cfe6f5;
        border-radius: 12px;
        padding: 16px 12px;
        box-shadow: 0 2px 6px rgba(14, 118, 168, 0.08);
    }
    div[data-testid="stMetric"] label {
        color: #0E76A8 !important;
        font-weight: 600;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton > button[kind="primary"] {
        background-color: #0E76A8;
        border: none;
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #0a5c84;
        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(14, 118, 168, 0.3);
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f4f8;
        border-radius: 8px 8px 0 0;
        padding: 8px 16px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0E76A8 !important;
        color: white !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f7fafc;
        border-right: 1px solid #e2e8f0;
    }
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #0E76A8;
    }

    /* Dataframes */
    div[data-testid="stDataFrame"] {
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #e2e8f0;
    }

    /* Dividers - subtler */
    hr {
        margin: 1.2rem 0;
        opacity: 0.3;
    }
</style>
""", unsafe_allow_html=True)

API_URL = "http://127.0.0.1:5001/predict"

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown(
        """
        This dashboard predicts **patient wait time** using a
        trained ML model based on registration, triage,
        urgency, staffing and day-of-week data.
        """
    )

    st.divider()
    st.subheader("⚙️ Model Info")
    st.markdown(
        """
        - **Model:** Linear Regression
        - **Features:** Nurse Ratio, Registration Time,
          Triage Time, Urgency, Day of Week
        - **API Endpoint:** `/predict`
        """
    )

    st.divider()
    st.subheader("🔌 API Status")
    try:
        health = requests.get("http://127.0.0.1:5001/", timeout=2)
        st.success("Connected ✅")
    except Exception:
        st.error("Not reachable ❌")

    st.divider()
    if st.button("🗑 Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()

# ---------------- HEADER ----------------
st.markdown("""
<div style='
    background: linear-gradient(135deg, #0E76A8 0%, #14a0d6 100%);
    padding: 28px 20px;
    border-radius: 16px;
    margin-bottom: 10px;
    box-shadow: 0 4px 14px rgba(14, 118, 168, 0.25);
'>
    <h1 style='text-align:center;color:white;margin-bottom:4px;'>
    🏥 Clinic Wait Time Prediction System
    </h1>
    <h4 style='text-align:center;color:#e6f4fb;font-weight:400;margin-top:0;'>
    Machine Learning Based Patient Wait Time Forecasting Dashboard
    </h4>
</div>
""", unsafe_allow_html=True)

st.divider()

tab1, tab2, tab3 = st.tabs(["🔍 Single Prediction", "📁 Batch Prediction (CSV)", "📜 History"])

# ============================================================
# TAB 1 : SINGLE PREDICTION
# ============================================================
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👩‍⚕️ Patient Information")

        nurse_ratio = st.number_input(
            "Nurse-to-Patient Ratio",
            min_value=1,
            value=3
        )

        reg_time = st.number_input(
            "Time to Registration (min)",
            min_value=0.0,
            value=10.0
        )

    with col2:
        st.subheader("🏥 Visit Details")

        triage_time = st.number_input(
            "Time to Triage (min)",
            min_value=0.0,
            value=15.0
        )

        urgency = st.selectbox(
            "Urgency Level",
            ["Low", "Medium", "High", "Critical"]
        )

        day_of_week = st.selectbox(
            "Day of Week",
            ["Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday"]
        )

    day_map = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
        "Friday": 4, "Saturday": 5, "Sunday": 6
    }

    # ---- Input validation ----
    warnings = []
    if reg_time > 120:
        warnings.append("Registration time looks unusually high (>120 min). Please verify.")
    if triage_time > 120:
        warnings.append("Triage time looks unusually high (>120 min). Please verify.")
    if nurse_ratio > 20:
        warnings.append("Nurse-to-patient ratio looks unusually high. Please verify.")

    for w in warnings:
        st.warning(f"⚠ {w}")

    st.divider()

    if st.button("🔍 Predict Wait Time", use_container_width=True, type="primary"):

        input_data = {
            "Nurse-to-Patient Ratio": [nurse_ratio],
            "Time to Registration (min)": [reg_time],
            "Time to Triage (min)": [triage_time],
            "Urgency Level": [urgency],
            "dayofweek": [day_map[day_of_week]]
        }

        try:
            with st.spinner("Running prediction model..."):
                response = requests.post(API_URL, json=input_data, timeout=10)

            if response.status_code == 200:

                result = response.json()
                wait_time = float(result["predicted_wait_time"])

                # Save to history
                st.session_state.history.append({
                    "Time": datetime.now().strftime("%H:%M:%S"),
                    "Nurse Ratio": nurse_ratio,
                    "Reg Time": reg_time,
                    "Triage Time": triage_time,
                    "Urgency": urgency,
                    "Day": day_of_week,
                    "Predicted Wait (min)": round(wait_time, 1)
                })

                st.divider()
                st.subheader("📊 Prediction Results")

                c1, c2, c3 = st.columns(3)
                with c1:
                    st.metric("⏱ Predicted Wait Time", f"{wait_time:.1f} min")
                with c2:
                    st.metric("🚑 Urgency Level", urgency)
                with c3:
                    st.metric("👩‍⚕️ Nurse Ratio", nurse_ratio)

                # ---- Gauge chart ----
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=wait_time,
                    title={"text": "Wait Time (min)"},
                    gauge={
                        "axis": {"range": [0, 150]},
                        "bar": {"color": "#0E76A8"},
                        "steps": [
                            {"range": [0, 60], "color": "#d4f4dd"},
                            {"range": [60, 90], "color": "#fff3cd"},
                            {"range": [90, 150], "color": "#f8d7da"},
                        ],
                    }
                ))
                fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
                st.plotly_chart(fig, use_container_width=True)

                st.divider()
                st.subheader("💡 Recommendation")

                if urgency == "Critical":
                    st.error("🚨 Immediate attention required. Prioritize patient treatment.")
                elif wait_time > 90:
                    st.warning("⚠ Very High Waiting Time Expected. Consider adding more staff.")
                elif wait_time > 60:
                    st.warning("⏳ High Waiting Time Expected. Monitor patient flow.")
                else:
                    st.success("✅ Normal Patient Flow.")

                st.divider()
                st.subheader("🚦 Delay Status")

                if wait_time > 120:
                    st.error("🔴 Critical Delay Alert")
                elif wait_time > 60:
                    st.warning("🟡 Moderate Delay Alert")
                else:
                    st.success("🟢 Normal Flow")

            else:
                st.error(f"❌ API returned error (status {response.status_code}): {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("⚠ Could not connect to Flask API. Make sure app.py (backend) is running on port 5001.")
        except requests.exceptions.Timeout:
            st.error("⚠ Request timed out. The API took too long to respond.")
        except Exception as e:
            st.error(f"⚠ Unexpected error: {e}")

# ============================================================
# TAB 2 : BATCH PREDICTION
# ============================================================
with tab2:
    st.subheader("📁 Batch Prediction from CSV")
    st.markdown(
        """
        Upload a CSV with these exact columns:
        `Nurse-to-Patient Ratio`, `Time to Registration (min)`,
        `Time to Triage (min)`, `Urgency Level`, `dayofweek`
        (dayofweek as 0=Monday ... 6=Sunday)
        """
    )

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Preview:")
            st.dataframe(df.head(), use_container_width=True)

            required_cols = {
                "Nurse-to-Patient Ratio", "Time to Registration (min)",
                "Time to Triage (min)", "Urgency Level", "dayofweek"
            }

            if not required_cols.issubset(df.columns):
                st.error(f"❌ CSV is missing required columns: {required_cols - set(df.columns)}")
            else:
                if st.button("🔍 Run Batch Prediction", type="primary"):
                    results = []
                    progress = st.progress(0, text="Predicting...")

                    for i, row in df.iterrows():
                        payload = {
                            "Nurse-to-Patient Ratio": [row["Nurse-to-Patient Ratio"]],
                            "Time to Registration (min)": [row["Time to Registration (min)"]],
                            "Time to Triage (min)": [row["Time to Triage (min)"]],
                            "Urgency Level": [row["Urgency Level"]],
                            "dayofweek": [row["dayofweek"]]
                        }
                        try:
                            resp = requests.post(API_URL, json=payload, timeout=10)
                            if resp.status_code == 200:
                                pred = resp.json()["predicted_wait_time"]
                            else:
                                pred = None
                        except Exception:
                            pred = None

                        results.append(pred)
                        progress.progress((i + 1) / len(df), text=f"Predicting... {i+1}/{len(df)}")

                    df["Predicted Wait Time (min)"] = results
                    st.success("✅ Batch prediction complete!")
                    st.dataframe(df, use_container_width=True)

                    csv_out = df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        "⬇ Download Results CSV",
                        data=csv_out,
                        file_name="wait_time_predictions.csv",
                        mime="text/csv"
                    )

        except Exception as e:
            st.error(f"⚠ Error reading CSV: {e}")

# ============================================================
# TAB 3 : HISTORY
# ============================================================
with tab3:
    st.subheader("📜 Prediction History (this session)")

    if len(st.session_state.history) == 0:
        st.info("No predictions made yet. Go to 'Single Prediction' tab to get started.")
    else:
        hist_df = pd.DataFrame(st.session_state.history)
        st.dataframe(hist_df, use_container_width=True)

        # Trend chart
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            y=hist_df["Predicted Wait (min)"],
            x=hist_df["Time"],
            mode="lines+markers",
            line=dict(color="#0E76A8")
        ))
        fig2.update_layout(
            title="Predicted Wait Time Trend (this session)",
            xaxis_title="Time",
            yaxis_title="Wait Time (min)",
            height=350
        )
        st.plotly_chart(fig2, use_container_width=True)

        csv_hist = hist_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇ Download History CSV",
            data=csv_hist,
            file_name="prediction_history.csv",
            mime="text/csv"
        )

# ---------------- FOOTER ----------------
st.divider()

APP_VERSION = "v1.1.0"

# ---------------- FOOTER ----------------
st.divider()

APP_VERSION = "v1.1.0"

st.markdown(
    f"""
    <div style='
        text-align:center;
        padding: 14px 10px;
        margin-top: 10px;
        background-color: #f7fafc;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
    '>
        <p style='color:#0E76A8; margin-bottom:4px; font-weight:600;'>
            🏥 Clinic Wait Time Prediction System • Built with Streamlit
        </p>
        <p style='color:#94a3b8; font-size:0.8em; margin-top:0;'>
            {APP_VERSION} &nbsp;|&nbsp; Last loaded: {datetime.now().strftime('%d %b %Y, %I:%M %p')}
            &nbsp;|&nbsp; Predictions this session: {len(st.session_state.history)}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
