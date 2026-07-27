# 🌱 Eco-Friendly Product Sales Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)

<a href="https://ecofreindlyappuctregression-nhw8zsnzsqknj8gswsgp4y.streamlit.app/">
<img src="https://img.shields.io/badge/🚀%20Launch%20Live%20App-Streamlit-red?style=for-the-badge&logo=streamlit">
</a>

</div>

---

## 📌 Project Overview

**Eco-Friendly Product Sales Prediction** is an end-to-end Machine Learning project that predicts the **weekly sales of eco-friendly products** using marketing activities, customer footfall, online search trends, weather conditions, seasonal information, and holiday effects.

The model is deployed as an interactive **Streamlit Web Application**, allowing users to enter business-related inputs and instantly receive predicted weekly sales along with estimated monthly, quarterly, and yearly sales.

---

# 🌐 Live Demo

<div align="center">

<a href="https://ecofreindlyappuctregression-nhw8zsnzsqknj8gswsgp4y.streamlit.app/">
<img src="https://img.shields.io/badge/🚀%20Open%20Live%20Application-Streamlit-red?style=for-the-badge&logo=streamlit">
</a>

</div>

---

## ✨ Key Features

- 🌱 Weekly Sales Prediction
- 🗓 Estimated Monthly Sales
- 📊 Estimated Quarterly Sales
- 📈 Estimated Yearly Sales
- ⚙️ Automated Feature Engineering
- 📋 Current Input Summary
- 🌐 Interactive Streamlit Dashboard
- 🤖 End-to-End Machine Learning Pipeline

---

# 📊 Dataset Features

## 🌍 Business Information

- Region
- Week Start Date

## 📈 Marketing & Customer Features

- Marketing Spend
- Store Visits
- Google Trend Score
- Holiday Flag

## 🌤 Environmental Features

- Average Temperature

## 🎯 Target Variable

- Weekly Sales

---

# ⚙️ Feature Engineering

Several custom features were engineered to improve model performance.

### 📌 Year

Extracted from the week start date to capture yearly sales trends.

---

### 📌 Month

Captures monthly seasonality in sales.

---

### 📌 Quarter

Represents quarterly business patterns.

---

### 📌 Week Number

Captures weekly seasonal effects.

---

### 📌 Marketing × Google Trend

```text
marketing_spend × google_trend_score
```

Measures the combined effect of marketing campaigns and online customer interest.

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

Captures the impact of marketing campaigns during holiday weeks.

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
| Linear Regression | XX.XX | XX.XX | XX.XX |
| Ridge Regression | XX.XX | XX.XX | XX.XX |
| Lasso Regression | XX.XX | XX.XX | XX.XX |
| **🏆 Polynomial Linear Regression** | **XX.XX** | **XX.XX** | **XX.XX** |

> Replace the above values with your actual model evaluation metrics.

---

# 🏆 Best Performing Model

**Polynomial Linear Regression** achieved the best predictive performance and was selected as the final production model.

### Final Performance

| Metric | Score |
|--------|-------:|
| R² Score | **XX.XX** |
| MAE | **XX.XX** |
| RMSE | **XX.XX** |

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
Streamlit Deployment
```

---

# 📈 Model Evaluation Metrics

The regression models were evaluated using:

- 📈 R² Score
- 📉 Mean Absolute Error (MAE)
- 📊 Mean Squared Error (MSE)
- 📏 Root Mean Squared Error (RMSE)

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

- 🌱 Predicted Weekly Sales
- 🗓 Estimated Monthly Sales
- 📊 Estimated Quarterly Sales
- 📈 Estimated Yearly Sales
- 📋 Current Input Summary

> **Note:** Monthly, quarterly, and yearly sales are estimated by scaling the predicted weekly sales.

---

# 💻 Application Screenshots

## 🏠 Home Page

_Add your homepage screenshot here._

---

## 📊 Prediction Results

_Add your prediction output screenshot here._

---

## 📋 Sidebar Inputs

_Add your sidebar screenshot here._

---

# 🚀 Future Improvements

- Compare multiple regression algorithms
- Hyperparameter tuning
- Feature importance visualization
- Sales trend forecasting
- Interactive dashboards
- Download prediction reports
- Time-series forecasting

---

# 👨‍💻 Author

### **Dhruv Rapariya**

- 🔗 **LinkedIn:** https://www.linkedin.com/in/dhruv-rapariya
- 💻 **GitHub:** https://github.com/Dhruv-develop

---

<div align="center">

### ⭐ If you found this project helpful, please consider giving it a Star!

</div>
