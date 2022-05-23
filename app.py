import os, pandas as pd
from flask import Flask, render_template, url_for,request
import text_classifier

app = Flask(__name__)

posts = "Welcome to My App"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        text = request.form['name']
        count = text_classifier.classifier(text)
        return render_template('result.html', text = text, count = count)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 8000)

