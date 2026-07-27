# 🌱 Eco-Friendly Product Sales Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)

</div>

---

# 📌 Project Overview

**Eco-Friendly Product Sales Prediction** is an end-to-end Machine Learning project that predicts the **weekly sales of eco-friendly products** using marketing expenditure, customer footfall, Google search trends, weather conditions, seasonal information, and holiday effects.

The project compares multiple regression algorithms and selects the best-performing model based on evaluation metrics. The final model is deployed as an interactive **Streamlit Web Application**, enabling users to predict weekly sales and view estimated monthly, quarterly, and yearly sales.

---

# 🌐 Live Demo

<div align="center">

<a href="https://ecofreindlyappuctregression-nhw8zsnzsqknj8gswsgp4y.streamlit.app/">
<img src="https://img.shields.io/badge/🚀%20Open%20Live%20Application-Streamlit-red?style=for-the-badge&logo=streamlit">
</a>

</div>

---

# ✨ Key Features

- 🌱 Weekly Sales Prediction
- 📅 Estimated Monthly Sales
- 📊 Estimated Quarterly Sales
- 📈 Estimated Yearly Sales
- 🤖 Comparison of Multiple Regression Models
- 🏆 Best Model Selection
- ⚙️ Automated Feature Engineering
- 📋 Current Input Summary
- 🌐 Interactive Streamlit Dashboard
- 🔄 End-to-End Machine Learning Pipeline

---

# 📊 Dataset Features

## 🌍 Business Information

- Region
- Week Start Date

## 📈 Marketing & Customer Information

- Marketing Spend
- Store Visits
- Google Trend Score
- Holiday Flag

## 🌤 Environmental Information

- Average Temperature

## 🎯 Target Variable

- Weekly Sales

---

# ⚙️ Feature Engineering

To improve prediction accuracy, several custom features were engineered.

### 📌 Year

Extracted from the week start date to capture yearly sales trends.

---

### 📌 Month

Captures monthly seasonal variations.

---

### 📌 Quarter

Represents quarterly business patterns.

---

### 📌 Week Number

Captures weekly seasonal trends.

---

### 📌 Marketing × Google Trend

```text
marketing_spend × google_trend_score
```

Measures the combined impact of marketing campaigns and online customer interest.

---

### 📌 Marketing × Store Visits

```text
marketing_spend × store_visits
```

Represents the interaction between marketing investment and customer footfall.

---

### 📌 Holiday Marketing

```text
marketing_spend × holiday_flag
```

Captures the influence of marketing campaigns during holiday weeks.

---

### 📌 Visit Trend Ratio

```text
store_visits / (google_trend_score + 1)
```

Measures how effectively online search interest converts into store visits.

---

# 🤖 Machine Learning Models Evaluated

| Model | R² Score | MAE | RMSE |
|--------|---------:|---------:|---------:|
| Linear Regression | 0.2218 | 42.28 | 54.16 |
| Ridge Regression | 0.2222 | 42.28 | 54.14 |
| Lasso Regression | 0.1848 | 43.67 | 55.43 |
| ElasticNet Regression | 0.0760 | 47.64 | 59.01 |
| K-Nearest Neighbors Regressor | 0.6264 | 25.54 | 37.53 |
| **🏆 Polynomial Linear Regression** | **0.9048** | **14.95** | **18.95** |

---

# 🏆 Best Performing Model

**Polynomial Linear Regression** achieved the highest predictive performance among all evaluated regression algorithms and was selected as the final production model.

### Final Performance

| Metric | Score |
|--------|-------:|
| **R² Score** | **0.9048** |
| **Adjusted R² Score** | **0.9002** |
| **Mean Absolute Error (MAE)** | **14.95** |
| **Mean Squared Error (MSE)** | **358.95** |
| **Root Mean Squared Error (RMSE)** | **18.95** |

---

# 🔄 Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Feature Engineering
   │
   ▼
Data Preprocessing
   │
   ▼
Polynomial Feature Generation
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Best Model Selection
   │
   ▼
Model Deployment (Streamlit)
```

---

# 📈 Model Evaluation Metrics

The regression models were evaluated using:

- 📈 R² Score
- 📈 Adjusted R² Score
- 📉 Mean Absolute Error (MAE)
- 📊 Mean Squared Error (MSE)
- 📏 Root Mean Squared Error (RMSE)

### Performance Summary

- 🏆 Polynomial Linear Regression achieved the highest **R² Score (0.9048)**, explaining approximately **90.48%** of the variation in weekly sales.
- 📉 It also achieved the **lowest prediction errors** with an **MAE of 14.95** and **RMSE of 18.95**.
- 🥈 K-Nearest Neighbors Regressor ranked second with an **R² Score of 0.6264**.
- 📊 Linear Regression, Ridge Regression, Lasso Regression, and ElasticNet Regression were unable to effectively capture the nonlinear relationships within the dataset.

---

# 🛠️ Technology Stack

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 🤖 Scikit-learn
- 🌐 Streamlit
- 💾 Joblib

---

# 📂 Project Structure

```text
Eco-Friendly-Product-Sales-Prediction/
│
├── app.py
├── polyLR.pkl
├── ML_eco_freindly_product.ipynb
├── eco_friendly_product_sales.csv
├── requirements.txt
├── README.md
```

---

# 📈 Application Output

The application provides:

- 🌱 Weekly Sales Prediction
- 📅 Estimated Monthly Sales
- 📊 Estimated Quarterly Sales
- 📈 Estimated Yearly Sales
- 📋 Current Input Summary

> **Note:** Monthly, quarterly, and yearly sales are estimated by scaling the predicted weekly sales.

---

# 💻 Application Screenshots

## 🏠 Home Page

> Add a screenshot of your Streamlit home page here.

---

## 📊 Prediction Result

> Add a screenshot showing the predicted sales output.

---

## 📋 Sidebar Input Panel

> Add a screenshot of the sidebar with input controls.

---

# 🚀 Future Improvements

- Time Series Forecasting
- Hyperparameter Optimization
- Feature Importance Visualization
- Download Prediction Reports
- Interactive Sales Dashboard
- Model Explainability using SHAP
- Support Additional Regression Algorithms

---

# 👨‍💻 Author

## **Dhruv Rapariya**

🔗 **LinkedIn:**  
https://www.linkedin.com/in/dhruv-rapariya

💻 **GitHub:**  
https://github.com/Dhruv-develop

---

<div align="center">

### ⭐ If you found this project helpful, please consider giving it a Star!

</div>
