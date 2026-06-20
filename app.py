import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Heart Disease Analytics Dashboard",
    layout="wide"
)

# ------------------------------------------------
# TITLE
# ------------------------------------------------

st.title("❤️ Heart Disease Patient Analytics Dashboard")

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------

df = pd.read_csv(
    r"C:\Users\gopic\Desktop\Heart-Disease-Analytics\data\heart_cleaned.csv"
)

# ------------------------------------------------
# SIDEBAR FILTERS
# ------------------------------------------------

st.sidebar.header("Dashboard Filters")

# Gender Filter
gender = st.sidebar.selectbox(
    "Select Gender",
    ["All", "Male", "Female"]
)

# Age Range Filter
age_range = st.sidebar.slider(
    "Select Age Range",
    int(df["age"].min()),
    int(df["age"].max()),
    (
        int(df["age"].min()),
        int(df["age"].max())
    )
)

# Smoking Filter
smoker_filter = st.sidebar.selectbox(
    "Smoking Status",
    ["All", "Smoker", "Non-Smoker"]
)

# ------------------------------------------------
# CREATE FILTERED DATASET
# ------------------------------------------------

filtered_df = df.copy()

# Gender Filter Logic
if gender == "Male":
    filtered_df = filtered_df[
        filtered_df["male"] == 1
    ]

elif gender == "Female":
    filtered_df = filtered_df[
        filtered_df["male"] == 0
    ]

# Age Filter Logic
filtered_df = filtered_df[
    (filtered_df["age"] >= age_range[0]) &
    (filtered_df["age"] <= age_range[1])
]

# Smoking Filter Logic
if smoker_filter == "Smoker":
    filtered_df = filtered_df[
        filtered_df["currentSmoker"] == 1
    ]

elif smoker_filter == "Non-Smoker":
    filtered_df = filtered_df[
        filtered_df["currentSmoker"] == 0
    ]
# ------------------------------------------------
# KPI SECTION
# ------------------------------------------------

total_patients = len(filtered_df)

chd_cases = filtered_df["TenYearCHD"].sum()

if total_patients > 0:
    chd_percentage = round(
        (chd_cases / total_patients) * 100,
        2
    )
else:
    chd_percentage = 0

avg_age = round(
    filtered_df["age"].mean(),
    1
)

avg_bmi = round(
    filtered_df["BMI"].mean(),
    1
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Patients",
    total_patients
)

col2.metric(
    "CHD Cases",
    int(chd_cases)
)

col3.metric(
    "CHD Risk %",
    f"{chd_percentage}%"
)

col4.metric(
    "Average Age",
    avg_age
)

col5.metric(
    "Average BMI",
    avg_bmi
)

# ------------------------------------------------
# CHD DISTRIBUTION
# ------------------------------------------------

st.markdown("---")

st.subheader("CHD Distribution")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    x="TenYearCHD",
    data=filtered_df,
    ax=ax
)

ax.set_title(
    "10-Year Heart Disease Risk"
)

st.pyplot(fig)

# ------------------------------------------------
# AGE DISTRIBUTION
# ------------------------------------------------

st.markdown("---")

st.subheader("Age Distribution")

fig, ax = plt.subplots(figsize=(8,4))

sns.histplot(
    filtered_df["age"],
    bins=20,
    kde=True,
    ax=ax
)

ax.set_title(
    "Age Distribution"
)

st.pyplot(fig)

# ------------------------------------------------
# GENDER VS CHD
# ------------------------------------------------

st.markdown("---")

st.subheader("Gender vs CHD")

fig, ax = plt.subplots(figsize=(8,4))

sns.countplot(
    x="male",
    hue="TenYearCHD",
    data=filtered_df,
    ax=ax
)

ax.set_title(
    "Gender vs CHD"
)

st.pyplot(fig)

# ------------------------------------------------
# SMOKING VS CHD
# ------------------------------------------------

st.markdown("---")

st.subheader("Smoking vs CHD")

fig, ax = plt.subplots(figsize=(8,4))

sns.countplot(
    x="currentSmoker",
    hue="TenYearCHD",
    data=filtered_df,
    ax=ax
)

ax.set_title(
    "Smoking vs CHD"
)

st.pyplot(fig)

# ------------------------------------------------
# DIABETES VS CHD
# ------------------------------------------------

st.markdown("---")

st.subheader("Diabetes vs CHD")

fig, ax = plt.subplots(figsize=(8,4))

sns.countplot(
    x="diabetes",
    hue="TenYearCHD",
    data=filtered_df,
    ax=ax
)

ax.set_title(
    "Diabetes vs CHD"
)

st.pyplot(fig)
# ------------------------------------------------
# CORRELATION HEATMAP
# ------------------------------------------------

st.markdown("---")

st.subheader("Correlation Heatmap")

corr = filtered_df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(12,8))

sns.heatmap(
    corr,
    cmap="coolwarm",
    annot=False,
    ax=ax
)

ax.set_title("Correlation Heatmap")

st.pyplot(fig)

# ------------------------------------------------
# TOP RISK FACTORS
# ------------------------------------------------

st.markdown("---")

st.subheader("Top Risk Factors for CHD")

target_corr = corr["TenYearCHD"].drop("TenYearCHD")

target_corr = target_corr.sort_values()

fig, ax = plt.subplots(figsize=(10,6))

target_corr.plot(
    kind="barh",
    ax=ax
)

ax.set_title("Risk Factors Associated with CHD")

st.pyplot(fig)
model = joblib.load(
    r"C:\Users\gopic\Desktop\Heart-Disease-Analytics\models\chd_model.pkl"
)
st.markdown("---")
st.header("Heart Disease Risk Prediction")
age = st.number_input("Age", 30, 80, 50)

male = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

male = 1 if male == "Male" else 0

education = st.number_input(
    "Education Level",
    1,
    4,
    2
)

currentSmoker = st.selectbox(
    "Current Smoker",
    ["No", "Yes"]
)

currentSmoker = 1 if currentSmoker == "Yes" else 0

cigsPerDay = st.number_input(
    "Cigarettes Per Day",
    0,
    50,
    0
)

BPMeds = 0
prevalentStroke = 0

prevalentHyp = st.selectbox(
    "Hypertension",
    ["No", "Yes"]
)

prevalentHyp = 1 if prevalentHyp == "Yes" else 0

diabetes = st.selectbox(
    "Diabetes",
    ["No", "Yes"]
)

diabetes = 1 if diabetes == "Yes" else 0

totChol = st.number_input(
    "Total Cholesterol",
    100,
    600,
    230
)

sysBP = st.number_input(
    "Systolic BP",
    80,
    250,
    120
)

diaBP = st.number_input(
    "Diastolic BP",
    50,
    150,
    80
)

BMI = st.number_input(
    "BMI",
    10.0,
    50.0,
    25.0
)

heartRate = st.number_input(
    "Heart Rate",
    40,
    150,
    70
)

glucose = st.number_input(
    "Glucose",
    50,
    400,
    80
)
if st.button("Predict Risk"):

    prediction = model.predict([[
        male,
        age,
        education,
        currentSmoker,
        cigsPerDay,
        BPMeds,
        prevalentStroke,
        prevalentHyp,
        diabetes,
        totChol,
        sysBP,
        diaBP,
        BMI,
        heartRate,
        glucose
    ]])

    if prediction[0] == 1:
        st.error(
            "High Risk of Heart Disease within 10 Years"
        )
    else:
        st.success(
            "Low Risk of Heart Disease within 10 Years"
        )