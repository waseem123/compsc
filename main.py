from flask import Flask, url_for, render_template, request, redirect
import mysql.connector as connector
import _mysql_connector as c

from googletrans import Translator

app = Flask(__name__)


def connectivity():
    try:
        return connector.connect(host="localhost", user="root", password="", database="mpscdb")
    except c.MySQLInterfaceError as ex:
        print(ex)


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
    try:
        connection = connectivity()
        if (connection is not None):
            translator = Translator()
            sql = "SELECT `emp_id`, `emp_name`, `emp_designation`, `emp_organization`, `emp_mobileno` FROM `tbl_employee`"
            # sql = "SELECT a.`emp_id`, a.`emp_name`, a.`emp_designation`, a.`emp_organization`, a.`emp_mobileno`,b.category_name FROM `tbl_employee` AS a JOIN tbl_empcategory AS b ON a.emp_category=b.category_id WHERE a.emp_category=1"
            cursor = connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            # print(result)
            # for i in result:
            #     print(i[1])
            #     dat = translator.translate(i[5], src='en', dest='mr')
            #     print(dat.text)
        return render_template("employees.html", employeelist=result)
    except c.MySQLInterfaceError as ex:
        print("Exception", ex)
        return "<h2>COULD NOT MAKE A SECURE CONNECTION</h2>"
    except connector.errors.DatabaseError as ex:
        print("Exception", ex)
        return "<h2>COULD NOT MAKE A SECURE CONNECTION</h2>"


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


@app.route("/exams")
def exams():
    connection = connectivity()
    if (connection is not None):
        sql = "SELECT `exam_id`, `exam_title`, `exam_date`, `training_date`, `training_venue`  FROM `tbl_exam` ORDER BY exam_id DESC;"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
    return render_template("exams.html", centerlist=result)


@app.route("/new-exam", methods=['GET', 'POST'])
def newexam():
    examtitle = request.form['inputExamTitle']
    examdate = request.form['inputExamdate']
    trainingdate = request.form['inputTrainingdate']
    trainingvenue = request.form['inputTrainingvenue']
    connection = connectivity()
    if (connection is not None):
        sql = "INSERT INTO `tbl_exam`(`exam_title`, `exam_date`, `training_date`, `training_venue`) VALUES ('{}','{}','{}','{}')".format(examtitle,examdate,trainingdate,trainingvenue)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    # return render_template("exams.html", centerlist=result)
        return "<script>alert('Exam Added successfully'); location.href='exams';</script>"

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
        sql = "INSERT INTO `tbl_allotment`(`exam_center_id`, `emp_id`, `appointed_designation`,`training_date`, `exam_date`, `no_of_sessions`,`status`) VALUES ({},{},'{}','{}','{}',{},1)"

        cursor = connection.cursor()
        cursor.execute(sql.format(centerid, empid, designation, trainingdate, examdate, sessions))
        connection.commit()
        cursor.close()
    return "<script>alert('Allotment successful'); location.href='exam-allotments';</script>"


@app.route("/exam-allotments")
def examallotments():
    connection = connectivity()
    if (connection is not None):
        sql = "SELECT a.mapping_id, a.exam_center_id, c.center_name, a.emp_id, b.emp_name, a.appointed_designation, a.training_date, a.exam_date, a.no_of_sessions, a.status FROM tbl_allotment AS a JOIN tbl_employee AS b ON a.emp_id = b.emp_id JOIN tbl_examcenter AS c ON a.exam_center_id = c.center_id"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        print(result)
    return render_template("examallotments.html", allotmentlist=result)


@app.route("/institutewise-allotment/<string:centerid>")
def institutewiseallotments(centerid):
    connection = connectivity()
    if (connection is not None):
        sql = "SELECT c.center_name, a.emp_id, b.emp_name, b.emp_designation, b.emp_organization, a.appointed_designation, b.emp_mobileno, a.training_date, a.exam_date, a.no_of_sessions, a.status FROM tbl_allotment AS a JOIN tbl_employee AS b ON a.emp_id = b.emp_id JOIN tbl_examcenter AS c ON a.exam_center_id = c.center_id WHERE a.exam_center_id={}"
        cursor = connection.cursor()
        cursor.execute(sql.format(centerid))
        result = cursor.fetchall()
        cursor.close()
        print(result)
    return render_template("institutewiseallotments.html", allotmentlist=result,
                           institutename="(" + centerid + ") - " + result[0][0])


if __name__ == '__main__':
    app.run(debug=True)
