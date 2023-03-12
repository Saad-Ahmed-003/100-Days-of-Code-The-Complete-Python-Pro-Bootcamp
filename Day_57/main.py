from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/guest/<user>')
def home(user):
    respond1 = requests.get(url=f"https://api.genderize.io/?name={user}")
    respond2 = requests.get(url=f"https://api.agify.io/?name={user}")
    age1 = respond2.json()["age"]
    gender1 = respond1.json()["gender"]
    return render_template("index.html", name=user.capitalize(), gender=gender1, age=age1)


if __name__ == "__main__":
    app.run(debug=True)
