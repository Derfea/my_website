from flask import Flask, request, render_template

app = Flask(__name__)

class Item():
    def __init__(self, name, amounts):
        self.name = name
        self.amounts = amounts


@app.route("/")
def hello():

    # Items = [
    #     Item("Apples", 5),
    #     Item("Computer", 1),
    #     Item("Pear", 4)
    # ]

    Items = [
        {"name": "Apples", "amounts": 5},
        {"name": "Computer", "amounts": 1},
        {"name": "Pear", "amounts": 4}
    ]

    for item in Items:
        item["amounts"] = item["amounts"] * 2

    person = ("Chikamso", "Kanu")

    output = render_template("start.html", person=person , Items=Items)
    return output


@app.route("/test")
def test():
    args =  request.args
    age = args.get("age")
    name = args.get("name")

    return render_template("test.html", name = name, age = age)


@app.route("/profile")
def profile():
    return render_template("Profile.html")


@app.route("/roblox")
def roblox():
    return render_template("Roblox.html")


@app.route("/Minecraft")
def minecraft():
    return render_template("Minecraft.html")


@app.route("/Fortnite")
def fortnite():
    return render_template("Fortnight.html")
#
#
# @app.route("/Company")
# def company():
#     company1 = request.args.get("company")
#     money = request.args.get("money")
#     good = request.args.get("good")
#
#     # table1 = []
#     # for x in range(1, 50):
#     #     table1.append((x, x*money))
#     # print(table1)
#
#     return render_template("Company.html",
#                            company=company1,
#                            money=money,
#                            good=good)
#
#
# @app.route("/currency")
# def currency():
#     currency1 = request.args.get("currency1")
#     currency2 = request.args.get("currency2")
#     rate = request.args.get("rate")
#
#     table1 = []
#     for x in range(1, 50):
#         table1.append((x, x*rate))
#     print(table1)
#
#     return render_template("currency.html",
#                            currency1=currency1,
#                            currency2=currency2,
#                            rate=float(rate),
#                            table1=table1)
#

@app.route("/money")
def money():
    currency1 = request.args.get("currency1")
    currency2 = request.args.get("currency2")
    rate = request.args.get("rate")

    # table1 = []
    # for x in range(1, 50):
    #     table1.append((x, x*rate))
    # print(table1)

    return render_template("money.html",
                           currency1=currency1,
                           currency2=currency2,
                           rate=rate
                           )
                           # table1=table1)
