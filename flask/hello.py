from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/ssafy")
def ssafy():
    return "방가방가룽~"

@app.route("/isitchristmas")
def christmas():
    if datetime.datetime.month == 12:
        if datetime.datetime.day == 25: 
            return"ㅇ"
    else:
        return"ㄴ"
# variable routing
@app.route("/greeting/<string:name>")
def greeting(name):
    return f"{name} 안녕하십니까? 인사 오지게 박습니다."

@app.route("/cube/<int:num>")
def cube(num):
    sq = num**3
    return f"{sq}"

@app.route("/dinner")
def dinner():
    menu = ["햄버거", "수육", "치킨"]
    dinner =  random.choice(menu)
    return render_template("dinner.html", dinner=dinner, menu=menu)

@app.route("/music")
def music():
    mlist = ["아이유-이름에게", "멜로망스-욕심", "태연-기억을 걷는 시간"]
    music = random.choice(mlist)
    return render_template("music.html", music=music, mlist=mlist)