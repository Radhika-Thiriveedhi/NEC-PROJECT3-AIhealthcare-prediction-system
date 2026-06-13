import streamlit as st

st.set_page_config(
    page_title="AI Healthcare System",
    layout="wide"
)

st.title("🏥 AI-Powered Healthcare Prediction & Resource Management System")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Patients", 125)
col2.metric("Doctors", 18)
col3.metric("Beds", 250)
col4.metric("Appointments", 76)

st.markdown("---")

st.subheader("System Overview")

st.info("Authentication & User Management")
st.info("Patient Management")
st.info("Doctor Management")
st.info("Appointment Scheduling")
st.info("Electronic Health Records")
st.info("AI Disease Prediction")
st.info("Treatment Recommendation")
st.info("Patient Outcome Prediction")
st.info("Bed Management")
st.info("Staff Scheduling")
st.info("Resource Allocation")
st.info("Medical Report Analysis")
st.info("Emergency Alerts")
st.info("AI Chatbot")
st.info("Analytics Dashboard")
st.info("Notifications")
st.info("Reporting")