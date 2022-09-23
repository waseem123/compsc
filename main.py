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
    connection = connectivity()
    if (connection is not None):
        sql = "SELECT `center_id`, `center_name`, `center_address`, `center_contact`, `strength`, `center_availability` FROM tbl_examcenter`"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

    return render_template("examcenters.html", centerlist=result)


@app.route("/new-allotment")
def newallotment():
    connection = connectivity()
    if (connection is not None):
        sql = "SELECT `emp_id`, `emp_name` FROM `tbl_employee`"
        cursor = connection.cursor()
        cursor.execute(sql)
        empresult = cursor.fetchall()
        cursor.close()

    if (connection is not None):
        sql = "SELECT `center_id`, `center_name` FROM `tbl_examcenter`"
        cursor = connection.cursor()
        cursor.execute(sql)
        centerresult = cursor.fetchall()
        cursor.close()
    return render_template("newallotment.html", employeedata=empresult, centerdata=centerresult)


@app.route("/make-allotment", methods=["GET", "POST"])
def makeallotment():
    empid = request.form['inputEmployee']
    centerid = request.form['inputExamcenter']
    designation = request.form['inputDesignation']
    trainingdate = request.form['inputTrainingdate']
    examdate = request.form['inputExamdate']
    sessions = request.form['no_of_session']

    print(empid, examdate, sessions, centerid)
    connection = connectivity()
    if (connection is not None):
        sql = "INSERT INTO `tbl_employe_institut_mapping`(`exam_center_id`, `emp_id`, `appointed_designation`,`training_date`, `exam_date`, `no_of_sessions`,`status`) VALUES ({},{},'{}','{}','{}',{},1)"

        cursor = connection.cursor()
        cursor.execute(sql.format(centerid, empid, designation, trainingdate, examdate, sessions))
        connection.commit()
        cursor.close()
    return "<script>alert('Allotment successful'); location.href='exam-allotments';</script>"


@app.route("/exam-allotments")
def examallotments():
    connection = connectivity()
    if (connection is not None):
        sql = "SELECT a.mapping_id, a.exam_center_id, c.center_name, a.emp_id, b.emp_name, a.appointed_designation, a.training_date, a.exam_date, a.no_of_sessions, a.status FROM tbl_employe_institut_mapping AS a JOIN tbl_employee AS b ON a.emp_id = b.emp_id JOIN tbl_examcenter AS c ON a.exam_center_id = c.center_id"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        print(result)
    return render_template("examallotments.html",allotmentlist = result)


if __name__ == '__main__':
    app.run(debug=True)
