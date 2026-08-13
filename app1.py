(file)


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Flower Species Predictor",
    page_icon="🌸",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🌸 Flower Species Prediction")
st.write("Enter the flower measurements below to predict its species.")


# -----------------------------
# Input sliders
# -----------------------------

st.subheader("Flower Measurements")

sepal_length = st.slider(
    "Sepal Length (cm)",
    min_value=4.0,
    max_value=8.0,
