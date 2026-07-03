# Week 5 - Deep Learning Image Classification System

##  Project Overview
This project is an end-to-end Deep Learning Image Classification System built using TensorFlow, Keras, OpenCV, and Streamlit. It classifies fruit images into multiple categories using Convolutional Neural Networks (CNN) and compares performance with a baseline ANN model.

The final model is deployed as an interactive web application using Streamlit.

---

##  Features
- Image preprocessing and augmentation
- ANN model (baseline comparison)
- CNN model (main classifier)
- Model optimization (Dropout, BatchNorm, EarlyStopping)
- Performance evaluation (Accuracy, Precision, Recall, F1-score)
- Confusion matrix and training graphs
- Streamlit web app for real-time image prediction

---

##  Dataset
The dataset contains multiple fruit categories such as:
- Blueberry
- Cactus Fruit
- Cherry varieties

Each class contains hundreds of labeled images.

---

## 🏗️ Project Structure
Week5-DeepLearning-ImageClassifier/
│
├── app.py # Streamlit application
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
├── dataset/ # Image dataset
├── models/ # Saved ANN & CNN models
├── notebooks/ # Jupyter notebooks (training)
├── reports/ # Evaluation reports
├── screenshots/ # App screenshots
├── utils/ # Helper scripts


---

## ⚙️ Tech Stack
- Python
- TensorFlow / Keras
- OpenCV
- NumPy / Pandas
- Matplotlib
- Scikit-learn
- Streamlit

---

## 🧪 How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Run Streamlit app
streamlit run app.py
📊 Model Performance
CNN outperforms ANN significantly in image classification tasks
Regularization techniques improved generalization
Data augmentation reduced overfitting
🌐 Deployment

The project is deployed using Streamlit Community Cloud.

Live Demo:

https://your-streamlit-app-url.streamlit.app
📌 Author

Ihsanullah Tanoli
Machine Learning Intern

📜 License

This project is for educational purposes.


---

# ⚠️ IMPORTANT

After pasting this:

1. Save file as:
```text
README.md
