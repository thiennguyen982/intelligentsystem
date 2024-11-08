import streamlit as st
import plotly.graph_objects as go


def reported_page():
    st.markdown(
        """
        <h1 style='text-align: center; 
                font-size: 50px; 
                color: #4CAF50;'>
            Business Operation Reported
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
                border-radius: 10px;'>
            Customer Retention Report
        </h4>
        <br></br>
        """,
        unsafe_allow_html=True,
    )

    # Sample data for continued and discontinued customers
    total_customers = 1000  # Example total number of customers
    stop_percentage = 35  # Percentage of customers who stopped using the service
    stop_count = int(
        total_customers * (stop_percentage / 100)
    )  # Number of discontinued customers
    continue_count = total_customers - stop_count  # Number of continued customers

    # Align all components in a single row using columns
    col1, col2, col3, col4 = st.columns(4)

    # Display the card for Continued Customers
    with col1:
        st.markdown(
            f"""
            <div style="text-align: center; background-color: #28a745; color: white; padding: 20px; border-radius: 10px;">
                <h3>{continue_count}</h3>
                <p>Continued Customers</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Creating a half-donut chart for Continued Customers
    continued_fig = go.Figure(
        go.Pie(
            values=[100 - stop_percentage, stop_percentage, 100],
            labels=["Continued", "", ""],
            hole=0.6,
            sort=False,
            marker_colors=["#28a745", "#d3d3d3", "white"],
            direction="clockwise",
            rotation=-90,
        )
    )

    continued_fig.update_traces(
        textinfo="none",  # Hide percentages on slices
        showlegend=False,  # Disable the legend for a cleaner look
    )

    continued_fig.update_layout(
        title="<b>Continued Customers</b>",
        annotations=[
            {
                "text": f"<b>{100 - stop_percentage}%</b>",
                "x": 0.5,
                "y": 0.1,
                "font_size": 20,
                "showarrow": False,
            }
        ],
        margin=dict(t=25, b=10, l=10, r=10),  # Reduce margins
        height=200,  # Set chart height to align with cards
        autosize=True,
    )

    # Display the Continued Customers half-donut chart
    with col2:
        st.plotly_chart(continued_fig, use_container_width=True)

    # Display the card for Discontinued Customers
    with col3:
        st.markdown(
            f"""
            <div style="text-align: center; background-color: #ff6b6b; color: white; padding: 20px; border-radius: 10px;">
                <h3>{stop_count}</h3>
                <p>Discontinued Customers</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Creating a half-donut chart for Stopped Customers
    stopped_fig = go.Figure(
        go.Pie(
            values=[stop_percentage, 100 - stop_percentage, 100],
            labels=["Stopped", "", ""],
            hole=0.6,
            sort=False,
            marker_colors=["#ff6b6b", "#d3d3d3", "white"],
            direction="clockwise",
            rotation=-90,
        )
    )

    stopped_fig.update_traces(
        textinfo="none",  # Hide percentages on slices
        showlegend=False,  # Disable the legend for a cleaner look
    )

    stopped_fig.update_layout(
        title="<b>Stopped Customers</b>",
        annotations=[
            {
                "text": f"<b>{stop_percentage}%</b>",
                "x": 0.5,
                "y": 0.1,
                "font_size": 20,
                "showarrow": False,
            }
        ],
        margin=dict(t=25, b=10, l=10, r=10),  # Reduce margins
        height=200,  # Set chart height to align with cards
        autosize=True,
    )

    # Display the Stopped Customers half-donut chart
    with col4:
        st.plotly_chart(stopped_fig, use_container_width=True)

    # Line chart showing trends for predicted vs actual continued customers over 12 months
    st.markdown(
        """
        <h4 style='text-align: center; 
                background-color: #4CAF50; 
                color: white; 
                padding: 15px; 
                border-radius: 10px;'>
            Monthly Trend: Predicted vs Actual Continued Customers
        </h4>
        """,
        unsafe_allow_html=True,
    )

    months = [
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
        "Dec",
    ]

    # Fluctuated data for actual and predicted continued customers
    actual_customers = [780, 810, 835, 870, 850, 890, 860, 920, 905, 870, 940]
    predicted_customers = [800, 820, 850, 880, 840, 900, 880, 910, 890, 880, 950, 920]

    # Create the figure for the line chart
    line_fig = go.Figure()

    # Add line for actual continued customers
    line_fig.add_trace(
        go.Scatter(
            x=months,
            y=actual_customers,
            mode="lines+markers",
            name="Actual Continued Customers",
            line=dict(color="#28a745", width=3),
            marker=dict(size=8),
        )
    )

    # Add line for predicted continued customers
    line_fig.add_trace(
        go.Scatter(
            x=months,
            y=predicted_customers,
            mode="lines+markers",
            name="Predicted Continued Customers",
            line=dict(color="#ff7f0e", width=3),
            marker=dict(size=8),
        )
    )

    # Update layout for the line chart
    line_fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Number of Customers",
        legend_title="Customer Data",
        margin=dict(t=40, b=40, l=40, r=40),
        autosize=True,  # Ensure the chart scales with container width
        title="Comparison of Predicted vs Actual Continued Customers",
    )

    # Display the line chart responsively
    st.plotly_chart(line_fig, use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Fluctuated data for customer counts
    continue_customers = [780, 810, 835, 870, 850, 890, 860, 920, 905, 870, 940, 910]
    stop_customers = [220, 190, 165, 130, 150, 110, 140, 80, 95, 130, 60, 90]

    # Calculate total customers and percentage for each category
    total_customers = [c + s for c, s in zip(continue_customers, stop_customers)]
    continue_percent = [
        round((c / total) * 100, 2)
        for c, total in zip(continue_customers, total_customers)
    ]
    stop_percent = [
        round((s / total) * 100, 2) for s, total in zip(stop_customers, total_customers)
    ]

    # Create the stacked bar chart
    stacked_fig = go.Figure()

    # Add bar for continued customers
    stacked_fig.add_trace(
        go.Bar(
            x=months,
            y=continue_percent,
            name="Continued (%)",
            marker=dict(color="#28a745"),
        )
    )

    # Add bar for stopped customers
    stacked_fig.add_trace(
        go.Bar(
            x=months,
            y=stop_percent,
            name="Stopped (%)",
            marker=dict(color="#ff6b6b"),
        )
    )

    # Update layout for the stacked bar chart
    stacked_fig.update_layout(
        barmode="stack",
        xaxis_title="Month",
        yaxis_title="Percentage (%)",
        legend_title="Customer Status",
        margin=dict(t=40, b=40, l=40, r=40),
        autosize=True,  # Ensure the chart scales with container width
        title="Monthly Customer Retention by Percentage",
    )

    # Display the stacked bar chart responsively
    st.plotly_chart(stacked_fig, use_container_width=True)

    # Line chart showing trends for customer retention by Internet Service
    st.markdown(
        """
        <h4 style='text-align: center; 
                background-color: #4CAF50; 
                color: white; 
                padding: 15px; 
                border-radius: 10px;'>
            Monthly Trend: Customer Retention by Internet Service
        </h4>
        """,
        unsafe_allow_html=True,
    )

    # Fluctuated data for each Internet Service type
    dsl_retention = [65, 68, 70, 72, 75, 73, 74, 76, 78, 80, 77, 79]
    fiber_retention = [85, 87, 88, 89, 90, 91, 92, 93, 94, 92, 93, 95]
    no_service_retention = [40, 42, 43, 41, 39, 38, 37, 36, 35, 34, 33, 32]

    # Create the line chart figure
    service_line_fig = go.Figure()

    # Add line for DSL retention
    service_line_fig.add_trace(
        go.Scatter(
            x=months,
            y=dsl_retention,
            mode="lines+markers",
            name="DSL Retention",
            line=dict(color="#1f77b4", width=3),
            marker=dict(size=8),
        )
    )

    # Add line for Fiber Optic retention
    service_line_fig.add_trace(
        go.Scatter(
            x=months,
            y=fiber_retention,
            mode="lines+markers",
            name="Fiber Optic Retention",
            line=dict(color="#2ca02c", width=3),
            marker=dict(size=8),
        )
    )

    # Add line for No Service retention
    service_line_fig.add_trace(
        go.Scatter(
            x=months,
            y=no_service_retention,
            mode="lines+markers",
            name="No Service Retention",
            line=dict(color="#d62728", width=3),
            marker=dict(size=8),
        )
    )

    # Update layout for the line chart
    service_line_fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Retention Percentage (%)",
        legend_title="Internet Service Type",
        title="Trend of Customer Retention by Internet Service",
        margin=dict(t=40, b=40, l=40, r=40),
        autosize=True,  # Ensure the chart scales with container width
    )

    # Display the line chart responsively
    st.plotly_chart(service_line_fig, use_container_width=True)

    # Calculate total retention for each month
    total_retention = [
        dsl + fiber + no_service
        for dsl, fiber, no_service in zip(
            dsl_retention, fiber_retention, no_service_retention
        )
    ]

    # Calculate percentage retention for each service type
    dsl_percent = [
        round((dsl / total) * 100, 2)
        for dsl, total in zip(dsl_retention, total_retention)
    ]
    fiber_percent = [
        round((fiber / total) * 100, 2)
        for fiber, total in zip(fiber_retention, total_retention)
    ]
    no_service_percent = [
        round((no_service / total) * 100, 2)
        for no_service, total in zip(no_service_retention, total_retention)
    ]

    # Create the stacked bar chart figure
    stacked_bar_fig = go.Figure()

    # Add bar for DSL retention
    stacked_bar_fig.add_trace(
        go.Bar(
            x=months,
            y=dsl_percent,
            name="DSL",
            marker=dict(color="#1f77b4"),
        )
    )

    # Add bar for Fiber Optic retention
    stacked_bar_fig.add_trace(
        go.Bar(
            x=months,
            y=fiber_percent,
            name="Fiber Optic",
            marker=dict(color="#2ca02c"),
        )
    )

    # Add bar for No Service retention
    stacked_bar_fig.add_trace(
        go.Bar(
            x=months,
            y=no_service_percent,
            name="No Service",
            marker=dict(color="#d62728"),
        )
    )

    # Update layout for the stacked bar chart
    stacked_bar_fig.update_layout(
        barmode="stack",
        xaxis_title="Month",
        yaxis_title="Retention Percentage (%)",
        legend_title="Internet Service Type",
        title="Monthly Change of Customer Retention by Internet Service",
        margin=dict(t=40, b=40, l=40, r=40),
        autosize=True,  # Ensure the chart scales with container width
    )

    # Display the stacked bar chart responsively
    st.plotly_chart(stacked_bar_fig, use_container_width=True)

    # New: Customer retention by gender (Male vs Female) - Bar Chart
    st.markdown(
        """
        <h4 style='text-align: center; 
                  background-color: #4CAF50; 
                  color: white; 
                  padding: 15px; 
                  border-radius: 10px;'>
            Customer Retention by Gender
        </h4>
        """,
        unsafe_allow_html=True,
    )

    # Sample data for male and female retention
    genders = ["Male", "Female"]
    retention = [80, 70]  # Retention percentage for Male and Female
    discontinued = [20, 30]  # Discontinued percentage for Male and Female

    # Create a bar chart
    gender_fig = go.Figure()

    gender_fig.add_trace(
        go.Bar(
            x=genders,
            y=retention,
            name="Retention",
            marker=dict(color="#28a745"),
        )
    )

    gender_fig.add_trace(
        go.Bar(
            x=genders,
            y=discontinued,
            name="Discontinued",
            marker=dict(color="#ff6b6b"),
        )
    )

    gender_fig.update_layout(
        barmode="group",
        xaxis_title="Gender",
        yaxis_title="Percentage",
        title="Customer Retention by Gender",
        margin=dict(t=40, b=40, l=40, r=40),
        legend_title="Customer Status",
        autosize=True,  # Ensure the chart scales with container width
    )

    # Display the grouped bar chart responsively
    st.plotly_chart(gender_fig, use_container_width=True)
