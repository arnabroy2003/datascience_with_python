import streamlit as st
import pickle

# load model and vectorizer
with open("model.pkl","rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl","rb") as f:
    vectorizer = pickle.load(f)

st.title("Spam Detector App")
st.write("Enter a message to check if it's spam or not.")
text = st.text_area("Message")

button = st.button("Predict")
if button:
     user_vector = vectorizer.transform([text])
     prediction = model.predict(user_vector)
     if prediction[0] == 1:
        st.error("Spam")
     else:
        st.success("Not Spam")


