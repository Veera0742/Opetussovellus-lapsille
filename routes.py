from app import app
from flask import render_template, request, session, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")
    if users.register(username, password):
        return redirect("/")
    else:
        return render_template("mistake.html")

@app.route("/login")
def login():
    return render_template("login.html")
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        return redirect("/start")
    else: 
        return render_template("mistake.html")

@app.route("/start")
def start():
    return render_template("start.html")
    
@app.route("/logout")
def logout():
    return redirect("/")

@app.route("/numbergame")
def numbergame():
    return render_template("numbergame.html")

@app.route("/lettergame")
def lettergame():
    return render_template("lettergame.html")