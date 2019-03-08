#encoding: utf-8
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "text/plain"})
    results = response.text
    return render_template('index.html', results=response.text)



if __name__ == '__main__':
    app.run(debug=True)
    