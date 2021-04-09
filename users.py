from db import db
from flask import session, request
from werkzeug.security import check_password_hash, generate_password_hash

def register(username, password): 
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
    db.session.execute(sql, {"username":username,"password":hash_value})
    db.session.commit()

def login(username, password):
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
        print("Väärä tunnus")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            print("Oikea tunnus ja salasana")
        else:
            print("Väärä salasana")
