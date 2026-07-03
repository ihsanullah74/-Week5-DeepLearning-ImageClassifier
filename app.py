import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Fruit Image Classifier",
    page_icon="🍓",
    layout="centered"
)

st.title("🍓 Fruit Image Classification System")
st.write("Upload an image and let the CNN model predict the fruit.")

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/best_cnn.keras")

model = load_model()

# ----------------------------
# Class Names
# ----------------------------
CLASSES = [
    "Blueberry",
    "Cactus fruit",
    "Cherry 1"
]

# ----------------------------
# Prediction History
# ----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# Upload Image
# ----------------------------
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize((128, 128))

    img = np.array(img)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    predicted_index = np.argmax(prediction)

    confidence = float(np.max(prediction))

    predicted_class = CLASSES[predicted_index]

    st.success(f"Prediction: {predicted_class}")

    st.info(f"Confidence: {confidence*100:.2f}%")

    st.session_state.history.append(
        f"{predicted_class} ({confidence*100:.2f}%)"
    )

# ----------------------------
# Prediction History
# ----------------------------
st.subheader("Prediction History")

if len(st.session_state.history) == 0:
    st.write("No predictions yet.")
else:
    for item in st.session_state.history:
        st.write("•", item)

# ----------------------------
# Reset Button
# ----------------------------
if st.button("Reset Prediction History"):
    st.session_state.history = []
    st.rerun()