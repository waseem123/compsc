from flask import Flask, url_for, render_template, request, redirect
import mysql.connector as connector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/tables")
def tables():
    return render_template("tables.html")

@app.route("/employees")
def employees():
    return render_template("employees.html")

@app.route("/exam-centers")
def examcenters():
    return render_template("examcenters.html")


if __name__ == '__main__':
    app.run(debug=True)
