import streamlit as st
import pandas as pd
import numpy as np

st.title("🏥 AI Healthcare Prediction & Resource Management System")

st.markdown("### Hospital Overview Dashboard")

# ==========================
# KPI CARDS
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Patients",
        "1,250",
        "+45"
    )

with col2:
    st.metric(
        "👨‍⚕️ Doctors",
        "85",
        "+2"
    )

with col3:
    st.metric(
        "🛏 Available Beds",
        "180",
        "-12"
    )

with col4:
    st.metric(
        "📅 Today's Appointments",
        "92",
        "+15"
    )

st.divider()

# ==========================
# PATIENT TREND
# ==========================

st.subheader("📈 Weekly Patient Visits")

patient_data = pd.DataFrame({
    "Day": [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ],
    "Patients": [
        120,
        140,
        135,
        160,
        180,
        170,
        150
    ]
})

st.line_chart(
    patient_data.set_index("Day")
)

# ==========================
# BED OCCUPANCY
# ==========================

st.subheader("🛏 Bed Occupancy")

bed_data = pd.DataFrame({
    "Category": [
        "Occupied",
        "Available"
    ],
    "Beds": [
        320,
        180
    ]
})

st.bar_chart(
    bed_data.set_index("Category")
)

# ==========================
# DISEASE DISTRIBUTION
# ==========================

st.subheader("🩺 Disease Distribution")

disease_data = pd.DataFrame({
    "Disease": [
        "Diabetes",
        "Heart",
        "Kidney",
        "Cancer"
    ],
    "Cases": [
        300,
        220,
        150,
        80
    ]
})

st.bar_chart(
    disease_data.set_index("Disease")
)

# ==========================
# RECENT APPOINTMENTS
# ==========================

st.subheader("📅 Recent Appointments")

appointments = pd.DataFrame({
    "Patient": [
        "Ravi",
        "Priya",
        "Kiran",
        "Suresh"
    ],
    "Doctor": [
        "Dr. Sharma",
        "Dr. Kumar",
        "Dr. Rao",
        "Dr. Patel"
    ],
    "Status": [
        "Approved",
        "Pending",
        "Approved",
        "Completed"
    ]
})

st.dataframe(
    appointments,
    use_container_width=True
)

# ==========================
# ALERTS
# ==========================

st.subheader("🚨 Hospital Alerts")

st.warning(
    "ICU Occupancy has reached 85%"
)

st.info(
    "15 New Lab Reports Uploaded Today"
)

st.success(
    "Resource Availability Stable"
)