import streamlit as st
import pandas as pd
import numpy as np

st.title("🛏️ Hospital Bed Management System")

# Sample Hospital Data
TOTAL_BEDS = 500
ICU_BEDS = 80
EMERGENCY_BEDS = 50

occupied_beds = st.slider(
    "Current Occupied Beds",
    0,
    TOTAL_BEDS,
    320
)

available_beds = TOTAL_BEDS - occupied_beds

icu_occupied = st.slider(
    "ICU Beds Occupied",
    0,
    ICU_BEDS,
    45
)

emergency_reserved = st.slider(
    "Emergency Beds Reserved",
    0,
    EMERGENCY_BEDS,
    20
)

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Beds", TOTAL_BEDS)

with col2:
    st.metric("Occupied Beds", occupied_beds)

with col3:
    st.metric("Available Beds", available_beds)

with col4:
    st.metric("ICU Beds", ICU_BEDS)

st.divider()

# Occupancy %
occupancy_rate = (occupied_beds / TOTAL_BEDS) * 100

st.subheader("📊 Occupancy Analysis")

st.progress(int(occupancy_rate))

st.write(
    f"Hospital Occupancy Rate: {occupancy_rate:.2f}%"
)

# AI Forecast Section
st.subheader("🤖 AI Bed Demand Forecast")

daily_patients = st.number_input(
    "Expected Patients Tomorrow",
    0,
    1000,
    150
)

forecast_beds = int(daily_patients * 0.7)

st.metric(
    "Predicted Beds Needed",
    forecast_beds
)

if forecast_beds > available_beds:
    st.error(
        "⚠️ Bed Shortage Expected Tomorrow"
    )
else:
    st.success(
        "✅ Sufficient Beds Available"
    )

# Ward Distribution
st.subheader("🏥 Ward Distribution")

ward_data = pd.DataFrame({
    "Ward": [
        "General",
        "ICU",
        "Emergency",
        "Maternity",
        "Pediatrics"
    ],
    "Beds": [
        220,
        ICU_BEDS,
        EMERGENCY_BEDS,
        80,
        70
    ]
})

st.bar_chart(
    ward_data.set_index("Ward")
)