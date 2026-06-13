import streamlit as st
import pandas as pd

st.title("👨‍⚕️ AI Staff Scheduling Optimization")

st.subheader("Hospital Workload Forecast")

patient_load = st.slider(
    "Expected Patient Load",
    0,
    1000,
    250
)

# AI Recommendation Logic
recommended_doctors = max(5, patient_load // 15)
recommended_nurses = max(10, patient_load // 8)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Recommended Doctors",
        recommended_doctors
    )

with col2:
    st.metric(
        "Recommended Nurses",
        recommended_nurses
    )

st.divider()

st.subheader("📅 Shift Allocation")

shift_data = pd.DataFrame({
    "Shift": [
        "Morning",
        "Afternoon",
        "Night"
    ],
    "Doctors": [
        int(recommended_doctors * 0.4),
        int(recommended_doctors * 0.35),
        int(recommended_doctors * 0.25)
    ],
    "Nurses": [
        int(recommended_nurses * 0.4),
        int(recommended_nurses * 0.35),
        int(recommended_nurses * 0.25)
    ]
})

st.dataframe(
    shift_data,
    use_container_width=True
)

st.bar_chart(
    shift_data.set_index("Shift")
)

st.divider()

st.subheader("🚨 Emergency Staffing")

emergency_cases = st.number_input(
    "Expected Emergency Cases",
    0,
    500,
    20
)

if emergency_cases > 50:
    st.error(
        "Additional Emergency Team Required"
    )
elif emergency_cases > 20:
    st.warning(
        "Prepare Backup Staff"
    )
else:
    st.success(
        "Current Staff Capacity Sufficient"
    )

st.divider()

st.subheader("🤖 AI Recommendation")

if patient_load > 500:
    st.warning("""
    High Patient Volume Expected.
    
    • Add Extra Doctors
    • Add Extra Nurses
    • Enable Overtime Shifts
    • Increase ICU Staff
    """)
else:
    st.success("""
    Staffing Levels Adequate.
    
    • Normal Shift Allocation
    • Standard Workforce Planning
    """)