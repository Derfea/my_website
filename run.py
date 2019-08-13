from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
     Items = ["Apples", "Pear", "Banana"]
     output = render_template("start.html", name="Chikamso Kanu", Items=Items)
     print(output)
     return output

@app.route("/test")
def test():
    print(request.args)
    return render_template("test.html", name="Chikamso Kanu")