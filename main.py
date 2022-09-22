from flask import Flask, url_for, render_template, request, redirect
import mysql.connector as connector

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to home page</h1>"


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
