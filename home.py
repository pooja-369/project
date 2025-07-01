import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)


st.title("Real Estate Data Science Application")

st.write("In this comprehensive capstone project, the primary focus was on leveraging data science techniques to provide insights, predictions, and recommendations in the real estate domain. The project unfolds through various stages, covering data gathering, cleaning, exploratory analysis, modeling, recommendation systems, and the deployment of a user-friendly application.")

st.write("The project commenced with the collection of real estate data, which was self-scraped from the 99acres website.")

st.write("In the Model Selection and Productionalization phase, an exhaustive comparison of various regression models was conducted to determine the most effective model for predicting property prices. The process involved implementing a detailed price prediction pipeline that incorporated encoding methods, ensuring the robustness and accuracy of the chosen model. The selected model was then deployed using Streamlit, creating an intuitive and user-friendly web interface for end-users")

st.write("This capstone project not only demonstrates proficiency in data science techniques such as feature engineering, exploratory analysis, and model building but also showcases the deployment of a real-world application, making valuable insights and recommendations accessible to end-users.")

st.sidebar.title("🏡 Price Prediction & Recommender System")