# 🌱 Eco-Friendly Product Sales Prediction

A Machine Learning web application that predicts **weekly sales of eco-friendly products** based on marketing activities, customer visits, seasonal trends, and weather conditions.

Built using **Python, Scikit-learn, Streamlit, and Feature Engineering**, the application provides an interactive interface for forecasting sales and estimating monthly, quarterly, and yearly projections.

---

## 🚀 Live Demo

🔗 Add your Streamlit deployment link here

Example:

https://your-app-name.streamlit.app

---

## 📌 Project Overview

This project predicts the **weekly sales** of eco-friendly products using a **Polynomial Linear Regression** model.

The application allows users to enter business-related features such as:

- Region
- Week Start Date
- Average Temperature
- Google Trend Score
- Marketing Spend
- Store Visits
- Holiday Indicator

The model then predicts:

- 📅 Weekly Sales
- 🗓 Estimated Monthly Sales
- 📊 Estimated Quarterly Sales
- 📈 Estimated Yearly Sales

> **Note:** Monthly, quarterly, and yearly values are estimated by scaling the predicted weekly sales.

---

## 🛠 Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

### Machine Learning

- Polynomial Linear Regression
- Scikit-learn Pipeline
- Custom Feature Engineering

---

## 📊 Dataset Features

| Feature | Description |
|----------|-------------|
| week_start | Week starting date |
| region | Sales region |
| avg_temp | Average weekly temperature |
| google_trend_score | Google search trend score |
| marketing_spend | Weekly marketing budget |
| store_visits | Weekly customer visits |
| holiday_flag | Indicates holiday week (0 = No, 1 = Yes) |
| sales | Target variable (Weekly Sales) |

---

## ⚙️ Feature Engineering

A custom **FeatureEngineer** class was created using **BaseEstimator** and **TransformerMixin**.

Generated Features:

- Year
- Month
- Quarter
- Week Number
- Marketing × Google Trend
- Marketing × Store Visits
- Marketing During Holidays
- Store Visits / Google Trend Ratio

These engineered features help improve the model's predictive performance.

---

## 🤖 Machine Learning Pipeline

The workflow includes:

1. Data Cleaning
2. Feature Engineering
3. Data Preprocessing
4. Polynomial Feature Generation
5. Polynomial Linear Regression Model
6. Prediction
7. Streamlit Deployment

---

## 💻 Streamlit Application

The web application provides:

- Interactive sidebar inputs
- Weekly sales prediction
- Estimated monthly, quarterly, and yearly sales
- Current input summary
- Model information
- Responsive user interface

---

## 📂 Project Structure

```
Eco-Friendly-Product-Sales-Prediction/
│
├── app.py
├── polyLR.pkl
├── requirements.txt
├── eco-friendly-product-dataset.csv
├── ML_eco_freindly_product.ipynb
├── README.md
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Eco-Friendly-Product-Sales-Prediction.git
```

Navigate to the project folder

```bash
cd Eco-Friendly-Product-Sales-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📷 Application Preview

Add screenshots of your Streamlit application here.

Example:

- Home Screen
- Prediction Result
- Sidebar Inputs

---

## 📈 Future Improvements

- Support multiple regression algorithms
- Model comparison dashboard
- Feature importance visualization
- Download prediction report
- Time-series forecasting
- Sales trend visualization

---

## 👨‍💻 Author

**Dhruv Rapariya**

- LinkedIn: https://www.linkedin.com/in/dhruv-rapariya
- GitHub: https://github.com/Dhruv-develop

---

## ⭐ If you found this project useful

Please consider giving the repository a **Star ⭐**.
