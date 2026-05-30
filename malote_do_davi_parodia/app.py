
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = "malote-do-davi"

users = {}

@app.route("/")
def index():
    if "user" in session:
        return redirect("/home")
    return redirect("/login")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        users[u] = {"password": p, "coins": 1000}
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        if u in users and users[u]["password"] == p:
            session["user"] = u
            return redirect("/home")
    return render_template("login.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("home.html",
                           user=session["user"],
                           coins=users[session["user"]]["coins"])

@app.route("/spin")
def spin():
    if "user" not in session:
        return redirect("/login")
    users[session["user"]]["coins"] += 100
    return redirect("/home")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

app.run(debug=True)
