import streamlit as st
import joblib
import numpy as np

st.title("🩺 AI Disease Prediction System")

disease = st.selectbox(
    "Select Disease",
    [
        "Diabetes",
        "Heart Disease",
        "Kidney Disease",
        "Cancer Risk"
    ]
)

# ==========================
# DIABETES
# ==========================

if disease == "Diabetes":

    model = joblib.load("models/diabetes_model.pkl")

    st.subheader("Diabetes Prediction")

    preg = st.number_input("Pregnancies", 0)
    glucose = st.number_input("Glucose", 0)
    bp = st.number_input("Blood Pressure", 0)
    skin = st.number_input("Skin Thickness", 0)
    insulin = st.number_input("Insulin", 0)
    bmi = st.number_input("BMI", 0.0)
    pedigree = st.number_input(
        "Diabetes Pedigree Function",
        0.0
    )
    age = st.number_input("Age", 1)

    if st.button("Predict Diabetes"):

        data = np.array([
            [
                preg,
                glucose,
                bp,
                skin,
                insulin,
                bmi,
                pedigree,
                age
            ]
        ])

        result = model.predict(data)[0]

        if result == 1:
            st.error("🔴 High Diabetes Risk")
            st.warning("Consult Endocrinologist")
        else:
            st.success("🟢 Low Diabetes Risk")

# ==========================
# HEART
# ==========================

elif disease == "Heart Disease":

    model = joblib.load("models/heart_model.pkl")

    age = st.number_input("Age", 1)
    chol = st.number_input("Cholesterol", 0)
    bp = st.number_input("Blood Pressure", 0)
    hr = st.number_input("Heart Rate", 0)
    cp = st.selectbox(
        "Chest Pain",
        [0, 1]
    )

    if st.button("Predict Heart Disease"):

        data = np.array([
            [
                age,
                chol,
                bp,
                hr,
                cp
            ]
        ])

        result = model.predict(data)[0]

        if result == 1:
            st.error("🔴 Heart Disease Risk")
            st.warning("Consult Cardiologist")
        else:
            st.success("🟢 Low Risk")

# ==========================
# KIDNEY
# ==========================

elif disease == "Kidney Disease":

    model = joblib.load("models/kidney_model.pkl")

    age = st.number_input("Age", 1)
    bp = st.number_input("Blood Pressure", 0)
    urea = st.number_input("Blood Urea", 0)
    creatinine = st.number_input(
        "Creatinine",
        0.0
    )

    if st.button("Predict Kidney Disease"):

        data = np.array([
            [
                age,
                bp,
                urea,
                creatinine
            ]
        ])

        result = model.predict(data)[0]

        if result == 1:
            st.error("🔴 Kidney Disease Risk")
            st.warning("Consult Nephrologist")
        else:
            st.success("🟢 Low Risk")

# ==========================
# CANCER
# ==========================

else:

    model = joblib.load("models/cancer_model.pkl")

    age = st.number_input("Age", 1)

    smoking = st.selectbox(
        "Smoking",
        [0, 1]
    )

    genetics = st.selectbox(
        "Genetics",
        [0, 1]
    )

    symptoms = st.slider(
        "Symptoms Severity",
        1,
        10
    )

    if st.button("Predict Cancer Risk"):

        data = np.array([
            [
                age,
                smoking,
                genetics,
                symptoms
            ]
        ])

        result = model.predict(data)[0]

        if result == 1:
            st.error("🔴 Cancer Risk Detected")
            st.warning("Consult Oncologist")
        else:
            st.success("🟢 Low Risk")