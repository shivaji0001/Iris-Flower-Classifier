import streamlit as st  # type: ignore
import pickle


# Load the trained model
with open("iris_model.pkl", "rb") as file:
    model = pickle.load(file)


# Page title
st.title("🌸 Iris Flower Classifier")

st.write(
    "Enter the measurements of an Iris flower "
    "to predict its species."
)


# Input 1
sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=5.1
)


# Input 2
sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=3.5
)


# Input 3
petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=1.4
)


# Input 4
petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.2
)


# Prediction button
if st.button("Predict Flower 🌸"):

    # Put user input into a list
    features = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    # Make prediction
    prediction = model.predict(features)[0]


    # Convert number into flower name
    classes = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    result = classes[prediction]


    # Display result
    st.success(f"Predicted Flower: {result}")
