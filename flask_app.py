from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("model.pkl","rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl","rb") as f:
    vectorizer = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        vector = vectorizer.transform([message])
        prediction = model.predict(vector)
        if prediction[0] == 1:
            result = "Spam"
        else:
            result = "Not Spam" 
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)