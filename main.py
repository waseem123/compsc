from flask import Flask, url_for, render_template, request, redirect
import mysql.connector as connector

app = Flask(__name__)


def connectivity():
    return connector.connect(host="localhost", user="root", password="", database="mpscdb")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/tables")
def tables():
    return render_template("tables.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/new-allotment")
def newallotment():
    return render_template("layout.html")


@app.route("/employees")
def employees():
    connection = connectivity()
    if (connection is not None):
        sql = "SELECT `emp_id`, `emp_name`, `emp_designation`, `emp_organization`, `emp_mobileno` FROM `tbl_employee`"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        # print(result)
    return render_template("employees.html", employeelist=result)


@app.route("/exam-centers")
def examcenters():
    return render_template("examcenters.html")


if __name__ == '__main__':
    app.run(debug=True)
