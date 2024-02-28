from flask import Flask, render_template, request, jsonify
import requests

API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b-it"
headers = {"Authorization": "Bearer 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"}

app = Flask(__name__)

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            output = query({"inputs": user_input})
            return render_template("index.html", output=output)
        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
