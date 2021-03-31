from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:testi@localhost:5433/postgres"
#db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

# information to the database

#hash_value = generate_password_hash(password)
#sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
#db.session.execute(sql, {"username":username,"password":hash_value})
#db.session.commit()

#sql = "SELECT password FROM users WHERE username=:username"
#result = db.session.execute(sql, {"username":username})
#user = result.fetchone()    
#if user == None:
    # TODO: invalid username
#else:
 #   hash_value = user[0]
  #  if check_password_hash(hash_value,password):
        # TODO: correct username and password
   # else:
        # TODO: invalid password