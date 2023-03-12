from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/427bb5220a9f9944117b")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)
