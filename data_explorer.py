import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    # Sample data, replace this with your actual dataset loading method (e.g., pd.read_csv)
    df = pd.read_csv("./data/raw_data/telco_customer_churn.csv")

    # Convert relevant columns to numeric, forcing errors to NaN (e.g., for TotalCharges)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")

    return df


# EDA Function to be called in the main app
def data_explorer():
    # Load data
    df = load_data()

    # Streamlit App Layout
    st.title("Data Explorer")

    # Custom Title Formatting
    def custom_title(title):
        st.markdown(
            f"""
            <h4 style='text-align: center; 
                    background-color: #4CAF50; 
                    color: white; 
                    padding: 15px; 
                    border-radius: 10px;'>
                {title}
            </h4>
            <br></br>
            """,
            unsafe_allow_html=True,
        )

    # Show data overview
    custom_title("Data Overview")
    st.write("Here is a quick overview of the dataset:")
    st.dataframe(df)

    # Descriptive statistics
    custom_title("Descriptive Statistics")
    st.write("Summary statistics for numerical columns:")
    st.write(df.describe())

    # Visualizations

    # 1. Distribution of numerical columns
    custom_title("Numerical Feature Distributions")
    col1, col2 = st.columns(2)  # Create two columns

    with col1:
        fig1 = px.histogram(df, x="Tenure", nbins=20, title="Tenure Distribution")
        st.plotly_chart(fig1)

    with col2:
        fig2 = px.histogram(
            df, x="MonthlyCharges", nbins=20, title="Monthly Charges Distribution"
        )
        st.plotly_chart(fig2)

    col1, col2 = st.columns(2)  # Create a second row of charts

    with col1:
        fig3 = px.histogram(
            df, x="TotalCharges", nbins=20, title="Total Charges Distribution"
        )
        st.plotly_chart(fig3)

    # 2. Categorical Feature Counts
    custom_title("Categorical Feature Counts")
    col1, col2 = st.columns(2)

    with col1:
        gender_counts = df["Gender"].value_counts().reset_index()
        gender_counts.columns = ["Gender", "Count"]
        fig4 = px.bar(gender_counts, x="Gender", y="Count", title="Gender Distribution")
        st.plotly_chart(fig4)

    with col2:
        partner_counts = df["Partner"].value_counts().reset_index()
        partner_counts.columns = ["Partner", "Count"]
        fig5 = px.bar(
            partner_counts, x="Partner", y="Count", title="Partner Distribution"
        )
        st.plotly_chart(fig5)

    col1, col2 = st.columns(2)

    with col1:
        dependents_counts = df["Dependents"].value_counts().reset_index()
        dependents_counts.columns = ["Dependents", "Count"]
        fig6 = px.bar(
            dependents_counts,
            x="Dependents",
            y="Count",
            title="Dependents Distribution",
        )
        st.plotly_chart(fig6)

    with col2:
        churn_counts = df["Churn"].value_counts().reset_index()
        churn_counts.columns = ["Churn", "Count"]
        fig7 = px.bar(churn_counts, x="Churn", y="Count", title="Churn Distribution")
        st.plotly_chart(fig7)

    # Continue the same approach for other figures

    # 3. Churn Analysis
    custom_title("Churn Analysis")
    col1, col2 = st.columns(2)

    with col1:
        fig10 = px.histogram(
            df, x="Gender", color="Churn", title="Churn by Gender", barmode="stack"
        )
        st.plotly_chart(fig10)

    with col2:
        fig11 = px.histogram(
            df, x="Partner", color="Churn", title="Churn by Partner", barmode="stack"
        )
        st.plotly_chart(fig11)

    col1, col2 = st.columns(2)

    with col1:
        fig12 = px.histogram(
            df,
            x="InternetService",
            color="Churn",
            title="Churn by Internet Service",
            barmode="stack",
        )
        st.plotly_chart(fig12)

    with col2:
        fig13 = px.histogram(
            df,
            x="Contract",
            color="Churn",
            title="Churn by Contract Type",
            barmode="stack",
        )
        st.plotly_chart(fig13)

    col1, col2 = st.columns(2)

    with col1:
        fig14 = px.histogram(
            df,
            x="PaymentMethod",
            color="Churn",
            title="Churn by Payment Method",
            barmode="stack",
        )
        st.plotly_chart(fig14)

    with col2:
        fig15 = px.histogram(
            df,
            x="PaperlessBilling",
            color="Churn",
            title="Churn by Paperless Billing",
            barmode="stack",
        )
        st.plotly_chart(fig15)

    # 4. Correlation Heatmap (Numerical Features)
    custom_title("Correlation Heatmap")
    corr = df[["Tenure", "MonthlyCharges", "TotalCharges"]].corr()
    fig16 = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
    st.plotly_chart(fig16)

    # Outlier Detection (Optional)
    custom_title("Outlier Detection")
    fig17 = px.box(
        df, y=["Tenure", "MonthlyCharges", "TotalCharges"], title="Outlier Detection"
    )
    st.plotly_chart(fig17)
