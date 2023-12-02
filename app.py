from flask import Flask
import gunicorn

app = Flask(__name__)


@app.route("/")
def render_home():
    return ("<h1 style='display: flex; height: 100vh;justify-content: center; align-items: center;'>"
            "Hello To Raspberry Pi Flask App Test Environment"
            "</h1>")


@app.route("/greetings/<string: name>")
def render_home(name):
    return (f"<h1 style='display: flex; height: 100vh;justify-content: center; align-items: center;'>"
            f"How are you {name}"
            "</h1>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
