# 📌Project 2- overview.

# Medical Cost Prediction Using Machine Learning Regression

A machine learning regression project for predicting individual medical insurance charges using the **Medical Cost Personal Dataset**.

## Project Overview

The objective is to build and compare regression models that learn relationships between demographic, lifestyle, and personal attributes and individual medical insurance charges.

**Workflow:** Data Collection → Data Cleaning → EDA → Visualization → Feature Engineering → Model Training → Evaluation → Prediction

## Objectives

- Understand the Medical Cost Personal Dataset
- Clean and preprocess the data
- Perform Exploratory Data Analysis (EDA)
- Analyze distributions and feature-target relationships
- Detect potential outliers
- Create meaningful interaction features
- Encode categorical variables
- Train multiple regression algorithms
- Evaluate models using MAE, RMSE, R², and MAPE
- Compare model performance
- Predict medical charges for unseen test observations

## Dataset

**Dataset:** Medical Cost Personal Dataset  
**Target:** `charges`

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

## Exploratory Data Analysis

The EDA stage examines the structure, distribution, and relationships in the dataset before model development.

### Statistical Overview

| Variable | Mean |
|---|---:|
| Age | 39.22 years |
| BMI | 30.66 |
| Children | 1.10 |
| Charges | 13,279.12 USD |

EDA includes:

- Descriptive statistics using `df.describe()`
- Medical charges distribution
- Log-transformed charges distribution
- Age vs. charges
- BMI vs. charges
- Smoker vs. charges
- Correlation analysis
- Outlier analysis

Potential outliers were examined using the IQR method. Extreme medical charges were not automatically removed because they may represent legitimate high-cost insurance cases.

## Feature Engineering

Interaction features were created to represent combined effects involving smoking status:

```python
df_fe["smoker_bmi"] = df_fe["smoker"] * df_fe["bmi"]
df_fe["smoker_age"] = df_fe["smoker"] * df_fe["age"]
