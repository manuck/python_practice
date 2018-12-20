import random
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hell():
    return "wow!"


@app.route("/greeting/<string:name>")
def greeting(name):
    return f"{name}야 들어왔니?"
    
    
@app.route("/google")
def google():
    return render_template("google.html")
    
# 사용자에게 정보 받기 1. 입력창을 보여준다.
@app.route("/lunch")
def lunch():
    return render_template("lunch.html")
    
@app.route("/menupick")
def menupick():
    name =  request.args.get("person")
    if name == "승만":    
        return f"{name}아 푸라닭 먹어락!!1"
    else :
        return f"{name}아 호식이나 먹어라"

# 메뉴 등록할 수 있도록 입력창 보여주는 페이지
@app.route("/menu/add")
def menu_add():
    return render_template("menu_add.html")

# 메뉴 등록
@app.route("/menu/create")
def menu_create():
    menu = request.args.get("menu")
    with open("menu.txt", "a") as file:
        file.write(menu+"\n")
    
    return render_template("menu_create.html", menu=menu)
    # return redirect("/menulist")


# 메뉴 추천
@app.route("/menu")
def menu():
    # 1. 파일을 불러와서 리스트에 담는다.
    file = open('menu.txt', 'r')
    menulist =  file.readlines()
    file.close()
    # 2. 리스트에서 하나를 뽑아서, 변수에 저장한다.
    menulist = random.choice(menulist)
    # 3. html에 추천된 것을 보여준다.
    return render_template("menu.html", menulist=menulist)