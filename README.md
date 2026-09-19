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

Example evaluation:

```text
Accuracy
Precision
Recall
F1-Score


import pypandoc

readme = r'''# Medical Cost Prediction Using Machine Learning Regression

A machine learning regression project that predicts individual medical insurance charges using the **Medical Cost Personal Dataset**.

The project follows an end-to-end Data Science workflow:

**Data Collection → Data Cleaning → EDA → Visualization → Feature Engineering → Feature Selection → Model Training → Evaluation → Prediction**

---

## 📌 Project-2 Overview

Medical insurance charges vary between individuals based on demographic and lifestyle-related attributes. The objective of this project is to build regression models that learn patterns from historical insurance data and predict the medical charge (`charges`) for an individual.

### Project Objectives

- Understand and analyze the Medical Cost Personal Dataset
- Clean and preprocess the dataset
- Perform Exploratory Data Analysis (EDA)
- Visualize distributions and feature-target relationships
- Engineer meaningful features
- Encode categorical variables
- Analyze feature relationships
- Train multiple regression algorithms
- Evaluate models using MAE, RMSE, R², and MAPE
- Compare model performance
- Generate predictions for unseen test data

---

## 📊 Dataset

### Medical Cost Personal Dataset

The dataset contains personal and demographic information used to predict individual medical insurance charges.

| Feature | Type | Description |
|---|---|---|
| `age` | Numerical | Age of the individual |
| `sex` | Categorical | Sex of the individual |
| `bmi` | Numerical | Body Mass Index |
| `children` | Numerical | Number of children/dependents |
| `smoker` | Categorical | Smoking status |
| `region` | Categorical | Residential region |
| `charges` | Numerical | Individual medical insurance charge |

**Target variable:** `charges`

The project uses the Medical Cost Personal Dataset as a regression dataset.

---

## 🔎 Exploratory Data Analysis

EDA was performed to understand the structure, distribution, and relationships within the dataset.

### Statistical Analysis

The project uses descriptive statistics to examine:

- Mean
- Standard deviation
- Minimum and maximum values
- Quartiles
- Distribution of numerical variables

Important descriptive statistics include:

- Mean Age: **39.22 years**
- Mean BMI: **30.66**
- Mean Children: **1.10**
- Mean Charges: **13,279.12 USD**

### EDA Visualizations

The project examines:

- Medical charges distribution
- Log-transformed medical charges distribution
- Age vs. Charges
- BMI vs. Charges
- Smoker vs. Charges
- Correlation heatmap
- Feature distributions
- Potential outliers

The analysis also examines the skewness of the target variable and uses log transformation for exploratory analysis of the highly skewed charge distribution.

---

## 🧹 Data Cleaning and Preprocessing

The preprocessing workflow includes:

1. Dataset inspection
2. Missing-value checking
3. Duplicate detection and handling
4. Outlier analysis
5. Categorical encoding
6. Numerical feature preparation
7. Train-test splitting

The dataset originally contains **1,338 records and 7 columns**. One duplicate record was identified and removed, leaving **1,337 records**.

Potential outliers were investigated using the IQR method. Extreme medical charges were not automatically removed because they may represent legitimate high-cost insurance cases.

---

## ⚙️ Feature Engineering

Additional features were created to help the regression models capture important relationships.

### Interaction Features

Two important interaction features were created:

```python
df_fe["smoker_bmi"] = df_fe["smoker"] * df_fe["bmi"]

df_fe["smoker_age"] = df_fe["smoker"] * df_fe["age"]
