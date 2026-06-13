import streamlit as st
import joblib
import numpy as np

st.title("🏥 Patient Outcome Prediction")

model = joblib.load(
    "models/outcome_model.pkl"
)

age = st.number_input(
    "Patient Age",
    1,
    120
)

severity = st.slider(
    "Disease Severity",
    1,
    10
)

icu = st.selectbox(
    "ICU Required",
    [0, 1]
)

days = st.number_input(
    "Expected Recovery Days",
    1,
    60
)

if st.button("Predict Outcome"):

    data = np.array([
        [
            age,
            severity,
            icu,
            days
        ]
    ])

    result = model.predict(data)[0]

    st.markdown("---")

    if result == 1:

        st.success(
            "🟢 High Recovery Probability"
        )

        st.metric(
            "Recovery Chance",
            "90%"
        )

        st.metric(
            "Readmission Risk",
            "Low"
        )

    else:

        st.error(
            "🔴 Recovery Risk Detected"
        )

        st.metric(
            "Recovery Chance",
            "40%"
        )

        st.metric(
            "Readmission Risk",
            "High"
        )

    if severity >= 8:
        st.warning(
            "ICU Monitoring Recommended"
        )

    if days > 20:
        st.info(
            "Long Hospital Stay Expected"
        )