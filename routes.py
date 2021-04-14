from app import app
from flask import Flask, render_template, request, session, redirect
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("mistake.html")

@app.route("/register")# methods=["POST"])
def register():
    return render_template("register.html")
#
#    username = request.form["username"]
 #   if len(username) < 1 or len(username) > 20:
  #      return render_template("mistake.html")

#    password1 = request.form["password1"]
#    password2 = request.form["password2"]
#    if password1 != password2:
#        return render_template("mistake.html")
#    if password1 == "":
#        return render_template("mistake.html")

#    if users.register(username, password1):
#        return redirect("/login")
#    else:
#        return render_template("mistake.html")

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