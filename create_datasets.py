import pandas as pd
import numpy as np
import os

os.makedirs("datasets", exist_ok=True)

np.random.seed(42)

# ==========================
# Diabetes Dataset
# ==========================

n = 500

diabetes = pd.DataFrame({
    "Pregnancies": np.random.randint(0, 15, n),
    "Glucose": np.random.randint(70, 220, n),
    "BloodPressure": np.random.randint(50, 120, n),
    "SkinThickness": np.random.randint(10, 60, n),
    "Insulin": np.random.randint(0, 600, n),
    "BMI": np.round(np.random.uniform(18, 45, n), 1),
    "DiabetesPedigreeFunction": np.round(np.random.uniform(0.1, 2.5, n), 3),
    "Age": np.random.randint(18, 80, n)
})

diabetes["Outcome"] = (
    (diabetes["Glucose"] > 140) &
    (diabetes["BMI"] > 30)
).astype(int)

diabetes.to_csv("datasets/diabetes.csv", index=False)

# ==========================
# Heart Disease Dataset
# ==========================

heart = pd.DataFrame({
    "Age": np.random.randint(20, 85, n),
    "Cholesterol": np.random.randint(120, 400, n),
    "BloodPressure": np.random.randint(80, 200, n),
    "HeartRate": np.random.randint(60, 200, n),
    "ChestPain": np.random.randint(0, 2, n)
})

heart["Outcome"] = (
    (heart["Cholesterol"] > 240) |
    (heart["BloodPressure"] > 140)
).astype(int)

heart.to_csv("datasets/heart.csv", index=False)

# ==========================
# Kidney Disease Dataset
# ==========================

kidney = pd.DataFrame({
    "Age": np.random.randint(20, 90, n),
    "BloodPressure": np.random.randint(60, 180, n),
    "BloodUrea": np.random.randint(10, 120, n),
    "Creatinine": np.round(np.random.uniform(0.5, 8.0, n), 2)
})

kidney["Outcome"] = (
    (kidney["Creatinine"] > 2.0) |
    (kidney["BloodUrea"] > 50)
).astype(int)

kidney.to_csv("datasets/kidney.csv", index=False)

# ==========================
# Cancer Dataset
# ==========================

cancer = pd.DataFrame({
    "Age": np.random.randint(20, 90, n),
    "Smoking": np.random.randint(0, 2, n),
    "Genetics": np.random.randint(0, 2, n),
    "Symptoms": np.random.randint(1, 10, n)
})

cancer["Outcome"] = (
    (cancer["Smoking"] == 1) &
    (cancer["Symptoms"] > 5)
).astype(int)

cancer.to_csv("datasets/cancer.csv", index=False)

# ==========================
# Patient Outcome Dataset
# ==========================

outcome = pd.DataFrame({
    "Age": np.random.randint(20, 90, n),
    "DiseaseSeverity": np.random.randint(1, 10, n),
    "ICURequired": np.random.randint(0, 2, n),
    "RecoveryDays": np.random.randint(1, 40, n)
})

outcome["Recovered"] = (
    outcome["DiseaseSeverity"] < 7
).astype(int)

outcome.to_csv("datasets/patient_outcomes.csv", index=False)

# ==========================
# Hospital Resources Dataset
# ==========================

resources = pd.DataFrame({
    "Day": np.arange(1, 501),
    "Patients": np.random.randint(50, 300, 500),
    "BedsUsed": np.random.randint(20, 250, 500),
    "VentilatorsUsed": np.random.randint(0, 50, 500),
    "OxygenUnitsUsed": np.random.randint(10, 150, 500)
})

resources.to_csv(
    "datasets/hospital_resources.csv",
    index=False
)

# ==========================
# Staff Dataset
# ==========================

staff = pd.DataFrame({
    "Day": np.arange(1, 501),
    "PatientLoad": np.random.randint(50, 300, 500),
    "Doctors": np.random.randint(5, 40, 500),
    "Nurses": np.random.randint(10, 80, 500)
})

staff.to_csv(
    "datasets/staff_data.csv",
    index=False
)

print("=" * 50)
print("All Healthcare Datasets Created Successfully")
print("=" * 50)

print("diabetes.csv")
print("heart.csv")
print("kidney.csv")
print("cancer.csv")
print("patient_outcomes.csv")
print("hospital_resources.csv")
print("staff_data.csv")