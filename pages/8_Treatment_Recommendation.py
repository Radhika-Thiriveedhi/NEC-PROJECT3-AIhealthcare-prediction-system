import streamlit as st

st.title("💊 AI Treatment Recommendation Engine")

disease = st.selectbox(
    "Select Disease",
    [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Cancer Risk"
    ]
)

if st.button("Generate Recommendation"):

    if disease == "Diabetes":

        st.success("Disease: Diabetes")

        st.subheader("👨‍⚕️ Recommended Specialist")
        st.info("Endocrinologist")

        st.subheader("🧪 Suggested Tests")
        st.write("""
        • HbA1c Test
        • Fasting Blood Sugar
        • Postprandial Blood Sugar
        """)

        st.subheader("💊 Medication Guidance")
        st.write("""
        • Metformin
        • Insulin (if required)
        """)

        st.subheader("🥗 Lifestyle Advice")
        st.write("""
        • Low Sugar Diet
        • Daily Exercise
        • Weight Management
        """)

    elif disease == "Heart Disease":

        st.success("Disease: Heart Disease")

        st.subheader("👨‍⚕️ Recommended Specialist")
        st.info("Cardiologist")

        st.subheader("🧪 Suggested Tests")
        st.write("""
        • ECG
        • Echocardiogram
        • Stress Test
        """)

        st.subheader("💊 Medication Guidance")
        st.write("""
        • Blood Pressure Medication
        • Cholesterol Control Medication
        """)

        st.subheader("🥗 Lifestyle Advice")
        st.write("""
        • Low Salt Diet
        • Avoid Smoking
        • Regular Walking
        """)

    elif disease == "Kidney Disease":

        st.success("Disease: Kidney Disease")

        st.subheader("👨‍⚕️ Recommended Specialist")
        st.info("Nephrologist")

        st.subheader("🧪 Suggested Tests")
        st.write("""
        • Kidney Function Test
        • Creatinine Test
        • Urine Analysis
        """)

        st.subheader("💊 Medication Guidance")
        st.write("""
        • Kidney Protection Medication
        • Blood Pressure Management
        """)

        st.subheader("🥗 Lifestyle Advice")
        st.write("""
        • Reduce Salt Intake
        • Stay Hydrated
        • Avoid Alcohol
        """)

    else:

        st.success("Disease: Cancer Risk")

        st.subheader("👨‍⚕️ Recommended Specialist")
        st.info("Oncologist")

        st.subheader("🧪 Suggested Tests")
        st.write("""
        • MRI Scan
        • CT Scan
        • Biopsy
        """)

        st.subheader("💊 Medication Guidance")
        st.write("""
        • Follow Doctor's Prescription
        • Chemotherapy (if needed)
        """)

        st.subheader("🥗 Lifestyle Advice")
        st.write("""
        • Balanced Nutrition
        • Regular Monitoring
        • Avoid Smoking
        """)