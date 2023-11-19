from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
#app.secret_key = "3b70c75bc80c498a726869560db6867d"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///user"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/newNote", methods=["POST"])
def new():
    return render_template("newNote.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form=["POST"]
    sql = "INSERT INTO notes (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")

@app.route("/save", methods=["POST"])
def save():
    return render_template("save.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["name"])