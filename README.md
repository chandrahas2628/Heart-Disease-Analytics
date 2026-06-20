# ❤️ Heart Disease Patient Analytics and Risk Factor Dashboard

## Project Overview

This project analyzes healthcare data to identify major risk factors associated with Coronary Heart Disease (CHD) and provides an interactive dashboard for analytics and risk prediction.

The project includes:

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Risk Factor Analysis
* Machine Learning Prediction
* Interactive Streamlit Dashboard

---

## Dataset Information

**Dataset:** Framingham Heart Study Dataset

**Total Records:** 4,240 Patients

**Total Features:** 16

### Target Variable

**TenYearCHD**

* 0 = No Coronary Heart Disease within 10 years
* 1 = Coronary Heart Disease within 10 years

### Features Used

* Age
* Gender
* Education
* Smoking Status
* Cigarettes Per Day
* Blood Pressure Medication
* Stroke History
* Hypertension
* Diabetes
* Total Cholesterol
* Systolic Blood Pressure
* Diastolic Blood Pressure
* BMI
* Heart Rate
* Glucose

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

## Project Workflow

### 1. Data Cleaning

* Checked missing values
* Handled null values
* Removed inconsistencies
* Saved cleaned dataset

### 2. Exploratory Data Analysis

* CHD Distribution Analysis
* Age Distribution Analysis
* Gender vs CHD
* Smoking vs CHD
* Diabetes vs CHD
* Blood Pressure Analysis
* Cholesterol Analysis
* BMI Analysis

### 3. Risk Factor Analysis

Correlation analysis identified the most influential risk factors:

1. Age
2. Systolic Blood Pressure
3. Hypertension
4. Glucose
5. Diabetes

### 4. Machine Learning

Model Used:

* Logistic Regression

Class imbalance was handled using:

```python
class_weight="balanced"
```

### Model Performance

* Accuracy: 66%
* Precision: 25%
* Recall: 63%
* F1 Score: 35%

### Why Recall Matters

In healthcare applications, identifying high-risk patients is more important than maximizing overall accuracy. Therefore, recall was prioritized during model evaluation.

---

## Dashboard Features

### KPI Cards

* Total Patients
* CHD Cases
* CHD Percentage
* Average Age
* Average BMI

### Interactive Filters

* Gender Filter
* Age Range Filter
* Smoking Status Filter

### Visualizations

* CHD Distribution
* Age Distribution
* Gender vs CHD
* Smoking vs CHD
* Diabetes vs CHD

### Risk Prediction

Users can enter patient health information and receive a prediction of:

* High Risk of Heart Disease
* Low Risk of Heart Disease

---

## Project Structure

Heart-Disease-Analytics/

├── data/

├── notebooks/

├── dashboard/

│ └── app.py

├── models/

│ └── chd_model.pkl

├── images/

├── reports/

├── README.md

└── requirements.txt

---

## Future Improvements

* Random Forest Model
* XGBoost Model
* Model Comparison Dashboard
* SHAP Explainability
* Cloud Deployment

---

## Author

**Chandrahas Palleda**
