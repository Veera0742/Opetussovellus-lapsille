from db import *
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import os

def register(username, password):
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()
    return redirect("/login")

def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()   
    if user == None:
        return redirect("/login")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            return redirect("/start")    
        else:
            return render_template("mistake.html")