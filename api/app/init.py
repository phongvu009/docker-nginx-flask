from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hellow Web"

if __name__ == "main":
    app.run(debug=True)