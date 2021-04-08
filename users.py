from db import db
from flask import session, request
from werkzeug.security import check_password_hash, generate_password_hash


def login(username, password):
    sql = "SELECT password, id FROM users WHERE username =: username"
    results = db.session.execute(sql, {"username": username})
    user = results.fetchone()
    if not user: 
        return False
    else:
        if check_password_hash(user[0], password):
            session["user_id"] = user[1]
            session["user_username"] = username
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["user_username"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (username, password)
                 VALUES (:username, :password,)"""
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)
