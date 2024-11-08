import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn.metrics import roc_curve


def training_result_page():
    st.markdown(
        """
        <h1 style='text-align: center; 
                font-size: 50px; 
                color: #4CAF50;' >
            Model Operation Reported
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.write("Percentage of customers who chose to stop using the service:")

    # Center the chart title using markdown
    st.markdown(
        """
        <h4 style='text-align: center; 
                background-color: #4CAF50; 
                color: white; 
                padding: 15px; 
                border-radius: 10px;' >
            Model Metrics Monitoring
        </h4>
        <br></br>
        """,
        unsafe_allow_html=True,
    )

    # Data for precision and recall trends from Jan to Nov
    data = {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
        ],
        "Precision": [0.85, 0.88, 0.87, 0.89, 0.86, 0.84, 0.88, 0.87, 0.86, 0.89, 0.90],
        "Recall": [0.80, 0.82, 0.81, 0.85, 0.84, 0.83, 0.85, 0.86, 0.84, 0.87, 0.80],
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Calculate F1 Score for each month
    df["F1 Score"] = (
        2 * (df["Precision"] * df["Recall"]) / (df["Precision"] + df["Recall"])
    )

    # Get the latest values for Precision, Recall, and F1 Score (last month in the dataset)
    precision_value = df["Precision"].iloc[-1]
    recall_value = df["Recall"].iloc[-1]
    f1_score_value = df["F1 Score"].iloc[-1]

    # Define a function to choose card color based on value
    def get_card_color(value):
        if value > 0.85:
            return "#4CAF50"  # Green
        elif value == 0.85:
            return "#ff9800"  # Yellow
        else:
            return "#ff6b6b"  # Red

    # Display the cards above the chart with dynamic background color
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div style="text-align: center; background-color: {get_card_color(precision_value)}; color: white; padding: 20px; border-radius: 10px;">
                <h3>{precision_value*100:.2f}%</h3>
                <p>Precision</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div style="text-align: center; background-color: {get_card_color(recall_value)}; color: white; padding: 20px; border-radius: 10px;">
                <h3>{recall_value*100:.2f}%</h3>
                <p>Recall</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div style="text-align: center; background-color: {get_card_color(f1_score_value)}; color: white; padding: 20px; border-radius: 10px;">
                <h3>{f1_score_value*100:.2f}%</h3>
                <p>F1 Score</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Create a Plotly line chart
    fig = go.Figure()

    # Add precision, recall, and F1 score lines to the chart
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Precision"],
            mode="lines+markers",
            name="Precision",
            line=dict(color="blue"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Recall"],
            mode="lines+markers",
            name="Recall",
            line=dict(color="red"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["F1 Score"],
            mode="lines+markers",
            name="F1 Score",
            line=dict(color="green"),
        )
    )

    # Add baseline line at 85%
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=[0.85] * len(df["Month"]),  # Line at 85%
            mode="lines",
            name="85% Baseline",
            line=dict(color="gray", dash="dash"),  # Dashed gray line
        )
    )

    # Customize layout
    fig.update_layout(
        title="Precision vs Recall vs F1 Score",
        xaxis_title="Month",
        yaxis_title="Value",
        template="plotly_dark",  # Optional: you can change the theme
        showlegend=True,
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Center the chart title using markdown
    st.markdown(
        """
        <h4 style='text-align: center; 
                background-color: #4CAF50; 
                color: white; 
                padding: 15px; 
                border-radius: 10px;' >
            Confusion matrix for last month
        </h4>
        <br></br>
        """,
        unsafe_allow_html=True,
    )

    # Confusion matrix values (based on November)
    TP = int(precision_value * 100)  # True Positives
    FP = int((1 - precision_value) * 100)  # False Positives
    FN = int((1 - recall_value) * 100)  # False Negatives
    TN = 100 - TP - FP - FN  # True Negatives

    # Construct confusion matrix
    confusion_matrix = np.array([[TP, FP], [FN, TN]])

    # Create text annotations for the confusion matrix
    annotations = [[f"{confusion_matrix[i][j]}" for j in range(2)] for i in range(2)]

    # Plot confusion matrix using Plotly with annotations
    fig_confusion = go.Figure(
        data=go.Heatmap(
            z=confusion_matrix,
            x=["Predicted Positive", "Predicted Negative"],
            y=["Actual Negative", "Actual Positive"],
            colorscale="cividis",
            showscale=True,
            text=annotations,  # Add the text annotations
            hoverinfo="text",  # Show text when hovering
        )
    )

    fig_confusion.update_layout(
        xaxis=dict(title="Predicted"),
        yaxis=dict(title="Actual"),
        template="plotly_dark",
    )

    # Display confusion matrix using Streamlit
    st.plotly_chart(fig_confusion, use_container_width=True)

    # ROC Curve
    # Center the chart title using markdown
    st.markdown(
        """
        <h4 style='text-align: center; 
                background-color: #4CAF50; 
                color: white; 
                padding: 15px; 
                border-radius: 10px;' >
            ROC curve
        </h4>
        <br></br>
        """,
        unsafe_allow_html=True,
    )

    # Generate simple data points for the demonstration
    x = np.linspace(0, 1, 100)  # X-axis from 0 to 1 (FPR range)

    # Linear ROC curve (example of a model that increases with linear relationship)
    y_linear = x  # TPR equals FPR in this simple example

    # Exponential ROC curve (example of a better model with increasing performance)
    y_exponential = 1 - np.exp(-x * 25)  # Exponential growth

    # Create a plotly figure
    fig_roc = go.Figure()

    # Add the linear ROC curve
    fig_roc.add_trace(
        go.Scatter(
            x=x,
            y=y_linear,
            mode="lines",
            name="Linear ROC Curve",
            line=dict(color="blue"),
        )
    )

    # Add the exponential ROC curve
    fig_roc.add_trace(
        go.Scatter(
            x=x,
            y=y_exponential,
            mode="lines",
            name="Exponential ROC Curve",
            line=dict(color="green"),
        )
    )

    # Add diagonal line (representing random model)
    fig_roc.add_trace(
        go.Scatter(
            x=[0, 1],
            y=[0, 1],
            mode="lines",
            name="Random Model",
            line=dict(color="gray", dash="dash"),
        )
    )

    # Update layout with titles and axis labels
    fig_roc.update_layout(
        title="Demonstration of ROC Curves",
        xaxis_title="False Positive Rate (FPR)",
        yaxis_title="True Positive Rate (TPR)",
        template="plotly_dark",
    )

    # Display the ROC curve in Streamlit
    st.plotly_chart(fig_roc, use_container_width=True)
