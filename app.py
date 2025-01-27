import streamlit as st

# Function to load HTML content from a file
def load_html(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Load and display index.html (like the home page in your app)
index_html = load_html("templates/index.html")
st.markdown(index_html, unsafe_allow_html=True)

# Some other Streamlit UI components
st.title("Student Performance Prediction")

# Inputs for prediction
gender = st.selectbox("Gender", ("Male", "Female"))
ethnicity = st.selectbox("Ethnicity", ("Group A", "Group B", "Group C", "Group D"))
parental_level_of_education = st.selectbox("Parental Level of Education", ("Some College", "High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree"))
lunch = st.selectbox("Lunch", ("Standard", "Free/Reduced"))
test_preparation_course = st.selectbox("Test Preparation Course", ("None", "Completed"))
reading_score = st.number_input("Reading Score", min_value=0, max_value=100)
writing_score = st.number_input("Writing Score", min_value=0, max_value=100)

# Prediction button and logic
if st.button("Predict"):
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        # Show prediction result
        st.subheader("Prediction Result")
        st.write(f"The predicted performance is: {results[0]}")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")

# Optionally, load and display home.html (if needed)
home_html = load_html("templates/home.html")
st.markdown(home_html, unsafe_allow_html=True)
