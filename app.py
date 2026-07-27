import streamlit as st
import joblib
import pandas as pd
from sklearn.base import BaseEstimator,TransformerMixin

st.set_page_config(
    page_title="Eco-Friendly Product Sales Prediction",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

.prediction{
    background:#1f77b4;
    padding:25px;
    border-radius:15px;
    color:white;
    text-align:center;
}

.metric{
    background:#ffffff;
    padding:15px;
    border-radius:10px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
}

</style>
""",unsafe_allow_html=True)


class FeatureEngineer(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = X.copy()


        # Date Features

        X["week_start"] = pd.to_datetime(
            X["week_start"],
            dayfirst=True
        )

        X["year"] = X["week_start"].dt.year
        X["month"] = X["week_start"].dt.month
        X["quarter_num"] = X["week_start"].dt.quarter
        X["week_no"] = X["week_start"].dt.isocalendar().week.astype(int)


        # Interaction Features


        # Marketing × Google Trend
        X["marketing_x_trend"] = (
            X["marketing_spend"] *
            X["google_trend_score"]
        )

        # Marketing × Store Visits
        X["marketing_x_visits"] = (
            X["marketing_spend"] *
            X["store_visits"]
        )

        # Holiday Marketing
        X["marketing_holiday"] = (
            X["marketing_spend"] *
            X["holiday_flag"]
        )

        # Ratio Feature

        X["visit_trend_ratio"] = (
            X["store_visits"] /
            (X["google_trend_score"] + 1)
        )

        return X


model = joblib.load('polyLR.pkl')


st.title("🌱 Eco-Friendly Product Sales Prediction")

st.caption(
    "Predict weekly sales of eco-friendly products using Machine Learning and Feature Engineering."
)

st.sidebar.header("📋 Input Features")

region = st.sidebar.selectbox("Region",["North","South","East","West"])

week_start = st.sidebar.date_input("Week Start")

avg_temp = st.sidebar.slider("Average Temperature (°C)",0,50,25)

google_trend_score = st.sidebar.slider("Google Trend Score",0,100,50)

marketing_spend = st.sidebar.number_input("Marketing Spend",1000,50000,5000)

store_visits = st.sidebar.number_input("Store Visits",0,5000,500)

holiday_flag = st.sidebar.selectbox("Holiday",["No","Yes"])

holiday_flag = 1 if holiday_flag=="Yes" else 0

col1,col2 = st.columns([2,1])

with col1:

    st.subheader("Prediction")

    if st.button("🚀 Predict Sales"):

        input_df = pd.DataFrame({
            "week_start": [week_start],
            "region": [region],
            "avg_temp": [avg_temp],
            "google_trend_score": [google_trend_score],
            "marketing_spend": [marketing_spend],
            "store_visits": [store_visits],
            "holiday_flag": [holiday_flag]
        })

        weekly_sales = model.predict(input_df)[0]

        monthly_sales = weekly_sales * 4.33
        quarterly_sales = weekly_sales * 13
        yearly_sales = weekly_sales * 52

        st.success("Prediction Completed Successfully!")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "📅 Weekly Sales",
            f"{weekly_sales:,.2f}"
        )

        c2.metric(
            "🗓 Monthly Sales (Est.)",
            f"{monthly_sales:,.2f}"
        )

        c3.metric(
            "📊 Quarterly Sales (Est.)",
            f"{quarterly_sales:,.2f}"
        )

        c4.metric(
            "📈 Yearly Sales (Est.)",
            f"{yearly_sales:,.2f}"
        )
        st.info("Monthly, Quarterly and Yearly values are estimated by scaling the predicted weekly sales.")


with col2:

    with st.expander("📋 Current Inputs", expanded=True):
        st.write(f"**Region:** {region}")
        st.write(f"**Week Start:** {week_start.strftime('%d-%m-%Y')}")
        st.write(f"**Temperature:** {avg_temp} °C")
        st.write(f"**Google Trend:** {google_trend_score}")
        st.write(f"**Marketing Spend:** ₹ {marketing_spend:,}")
        st.write(f"**Store Visits:** {store_visits:,}")
        st.write(f"**Holiday:** {'Yes' if holiday_flag else 'No'}")
st.divider()

with st.expander("📈 Model Information"):

    st.write("""
    **Algorithm**
    - Polynomial Linear Regression

    **Feature Engineering**
    - Year
    - Month
    - Quarter
    - Week Number
    - Marketing × Trend
    - Marketing × Visits
    - Holiday Marketing
    - Visit Trend Ratio

    **Deployment**
    - Streamlit
    - Scikit-Learn Pipeline
    """)

