## 📌 Project-1 Overview


# ❤️ Heart Disease Prediction

A Data Science and Machine Learning project focused on analyzing patient health data and predicting the presence of heart disease.

## 📌 Project Overview

Heart disease is one of the major health problems worldwide. Early identification of patients who may be at risk can help support better medical decision-making.

In this project, we explore a heart disease dataset, perform data preprocessing and exploratory data analysis (EDA), visualize important relationships between features, and build machine learning models to predict whether a patient is likely to have heart disease.

The complete analysis and implementation are available in the Jupyter Notebook:

`heartdiseaseproject.ipynb`

---

## 🎯 Objectives

The main objectives of this project are:

- Understand the heart disease dataset
- Perform data cleaning and preprocessing
- Analyze important patient characteristics
- Perform Exploratory Data Analysis (EDA)
- Visualize relationships between variables
- Identify important features related to heart disease
- Train machine learning classification models
- Evaluate model performance
- Predict the presence of heart disease

---

## 📊 Dataset

The dataset contains patient-related medical and demographic information that can be used to predict heart disease.

Typical features include:

| Feature | Description |
|---|---|
| Age | Age of the patient |
| Sex | Gender of the patient |
| Chest Pain | Type of chest pain experienced |
| Resting Blood Pressure | Resting blood pressure |
| Cholesterol | Serum cholesterol level |
| Fasting Blood Sugar | Fasting blood sugar level |
| Resting ECG | Resting electrocardiographic results |
| Maximum Heart Rate | Maximum heart rate achieved |
| Exercise Angina | Exercise-induced angina |
| ST Depression | ST depression induced by exercise |
| ST Slope | Slope of the peak exercise ST segment |
| Heart Disease | Target variable indicating presence/absence of heart disease |

> **Note:** The exact features depend on the dataset used in `heartdiseaseproject.ipynb`.

---

## 🔍 Exploratory Data Analysis

The project performs exploratory analysis to understand the dataset and identify patterns.

Some of the analysis includes:

- Dataset structure and dimensions
- Missing-value analysis
- Statistical summaries
- Distribution of numerical features
- Categorical feature analysis
- Correlation analysis
- Target-variable distribution
- Relationship between patient characteristics and heart disease

Visualizations are used to make the patterns easier to understand.

---

## 🧹 Data Preprocessing

Before training the machine learning models, the data is prepared through appropriate preprocessing steps.

The preprocessing may include:

- Handling missing values
- Removing or handling duplicate records
- Encoding categorical variables
- Feature scaling
- Separating features and target variable
- Splitting the dataset into training and testing sets

---

## 🤖 Machine Learning

This project treats heart disease prediction as a **binary classification problem**.

Machine learning algorithms can be trained to classify patients into two categories:

- `0` → No heart disease
- `1` → Heart disease

Depending on the notebook implementation, classification algorithms may include:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

---

## 📈 Model Evaluation

The trained models can be evaluated using several classification metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 📌Project 2- overview.

# Medical Cost Prediction Using Machine Learning Regression


Goal- Medical insurance charges vary between individuals based on demographic and lifestyle-related characteristics. This project applies an end-to-end **data science and machine learning regression workflow** to predict individual medical insurance charges.

### Workflow

**Data Collection → Data Cleaning → EDA → Visualization → Feature Engineering → Model Training → Evaluation → Prediction**

## Project Objectives

- Understand the Medical Cost Personal Dataset
- Inspect and clean the dataset
- Check missing values and duplicate records
- Analyze potential outliers
- Perform Exploratory Data Analysis (EDA)
- Visualize distributions and feature-target relationships
- Create meaningful interaction features
- Encode categorical variables
- Train and compare multiple regression algorithms
- Evaluate models using MAE, RMSE, R², and MAPE
- Select a model based on the defined evaluation criteria
- Generate predictions for unseen test observations
- Analyze prediction errors and residuals

---

## Dataset

**Dataset:** Medical Cost Personal Dataset  
**Target Variable:** `charges`

| Feature | Type | Description |
|---|---|---|
| `age` | Numerical | Age of the individual |
| `sex` | Categorical | Sex of the individual |
| `bmi` | Numerical | Body Mass Index |
| `children` | Numerical | Number of children/dependents |
| `smoker` | Categorical | Smoking status |
| `region` | Categorical | Residential region |
| `charges` | Numerical | Individual medical insurance charge |

### Dataset Summary

- **Original records:** 1,338
- **Columns:** 7
- **Duplicate records identified:** 1
- **Records after duplicate removal:** 1,337
- **Target variable:** `charges`
- **Source:** Medical Cost Personal Dataset (Kaggle)

---

# Exploratory Data Analysis

EDA was performed to understand the dataset before model development.

## Statistical Overview

| Variable | Mean |
|---|---:|
| Age | 39.22 years |
| BMI | 30.66 |
| Children | 1.10 |
| Charges | 13,279.12 USD |

The EDA includes:

- Descriptive statistics using `df.describe()`
- Medical charges distribution
- Log-transformed charges distribution
- Age vs. Charges analysis
- BMI vs. Charges analysis
- Smoker vs. Charges comparison
- Correlation analysis
- Outlier analysis

### EDA Analysis

The target variable `charges` has a wide distribution, indicating substantial variation in individual medical costs.

Smoking status shows a strong relationship with medical charges. Age and BMI were also examined against charges to understand their relationships with the target.

Potential outliers were examined using the IQR method. Extreme medical charges were not automatically removed because they may represent legitimate high-cost insurance cases.

---

# Data Cleaning and Preprocessing

The project performed the following preprocessing steps:

1. Inspected dataset shape, columns, and data types.
2. Checked for missing values.
3. Identified duplicate records.
4. Removed the identified duplicate record.
5. Examined potential outliers using the IQR method.
6. Prepared categorical variables for machine learning.
7. Prepared numerical and engineered features for model development.

---

# Feature Engineering

Interaction features were created to represent combined effects involving smoking status:

```python
df_fe["smoker_bmi"] = df_fe["smoker"] * df_fe["bmi"]
df_fe["smoker_age"] = df_fe["smoker"] * df_fe["age"]



