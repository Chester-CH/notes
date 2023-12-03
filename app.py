from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///" #getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT title FROM notes"))
    titles = result.fetchall()
    return render_template("index.html", count=len(titles), titles=titles) 

# @app.route("/newnote", methods=["POST"])
# def new():
#     return render_template("newnote.html")

# @app.route("/send", methods=["POST"])
# def send():
#     content = request.form=["POST"]
#     sql = "INSERT INTO notes (content) VALUES (:content)"
#     db.session.execute(sql, {"content":content})
#     db.session.commit()
#     return redirect("/")

# @app.route("/saved", methods=["POST"])
# def saved():    
#     title = request.form["title"]
#     content = request.form["content"]
#     sql = "INSERT INTO notes (title, content) VALUES (:title, :content)"
#     db.session.execute(sql, {"title":title})
#     db.session.execute(sql, {"content":content})
#     db.session.commit()
#     return render_template("saved.html")


##login, logout
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    print(result)
    user = result.fetchone()
    # print(user)
    # print(user.password)
    # print(check_password_hash(user.password,password))
    if not user:
        return "User name not found!"   
    else:
        #hash_value = user.password
        if check_password_hash(user.passowrd, password):
            print("hi!")

            return redirect("/")
        else:
            return "Your user or password in invalid, please check!"
    

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

##create new user
@app.route("/createuser")
def createuser():
    return render_template("createuser.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(text(sql), {"username":username, "password":hash_value})
    db.session.commit()
    return "New user created successfully!"

@app.route("/usercreated")
def usercreated():
    return "New user created successfully!"



# @app.route("/result", methods=["POST"])
# def result():
#     return render_template("result.html", name=request.form["name"])

if __name__ == '__main__':
    app.run(debug=True)

