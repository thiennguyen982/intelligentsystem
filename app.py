import streamlit as st
from streamlit_option_menu import option_menu
from reported_page import reported_page  # Import the reported page function
from training_result_page import training_result_page
from customer_classifier import customer_classifier_page
from data_explorer import data_explorer


# Set Streamlit page layout at the top of the script
st.set_page_config(layout="wide")


def main():
    # Sidebar menu with options
    with st.sidebar:
        selected = option_menu(
            "Dashboard",
            ["Reported", "Training Result", "Data Explorer", "Customer Classifier"],
            icons=["clipboard-data", "graph-up-arrow", "table", "person-bounding-box"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
        )

    # Display content based on selected page
    if selected == "Reported":
        reported_page()  # Call the function for the reported page
    elif selected == "Training Result":
        training_result_page()  # Call the function for the Training Result page
    elif selected == "Data Explorer":
        data_explorer()
    elif selected == "Customer Classifier":
        customer_classifier_page()


if __name__ == "__main__":
    main()
