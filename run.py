from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    Items = ["Apples", "Pear", "Banana"]

    return ""

@app.route("/test")
def test():
    paragraph = "<p>Chikamso is my name 54321, Lift of! <em>The person in the world</em></p>"
    return "<strong>Chikamso is my name</strong>" + paragraph