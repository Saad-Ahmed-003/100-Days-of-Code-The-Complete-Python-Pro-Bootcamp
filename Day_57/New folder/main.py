from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/427bb5220a9f9944117b")
all_posts = response.json()


@app.route('/blog')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id_num>')
def post(id_num):
    return render_template("post.html", posts=all_posts, id=id_num)


if __name__ == "__main__":
    app.run(debug=True)
