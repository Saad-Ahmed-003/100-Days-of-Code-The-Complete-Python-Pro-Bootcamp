from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess the number between 0 to 9</h1>' \
           '<img src="https://media3.giphy.com/media/StKiS6x698JAl9d6cx/giphy.gif?' \
           'cid=ecf05e47337a8934a3461cbd9c771471ed44a9b724de7ed4&rid=giphy.gif&ct=g">'


@app.route("/<int:num>")
def higher_or_lower(num):
    if num == 5:
        return '<h2>You found Me</h2>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif num > 5:
        return '<h2>Too high try again!</h2>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif num < 5:
        return '<h2>Too low try again</h2>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
