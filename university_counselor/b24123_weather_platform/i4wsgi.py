"""App entry point."""
import os
import sys
import json

import flask_login
from flask_cors import CORS

from flask import send_from_directory
from flask import request
from flask import url_for
from flask import redirect, session
from flask import Blueprint, render_template as rt
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, Response
from flask import jsonify
from flask_cors import CORS
from movie import create_app

import es_search
from i0whtether_bot import get_whether
import pandas as pd
import csv
import time

# from movie.domain.model import Director, Review, Movie

# from html_similarity import style_similarity, structural_similarity, similarity
# from common import set_js_file

app = create_app()
app.secret_key = "ABCabc123"
app.debug = True
CORS(app)
# --- total requirement ----


# ---start  数据库 ---
#  如果想更换为mysql/postgresql 可以修改这里
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus_data.db"

db = SQLAlchemy(app)

last_upload_filename = None
# --- end   数据库 ---
admin_list = ["admin@126.com", "greatabel1@126.com"]


class User(db.Model):
    """Create user table"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    nickname = db.Column(db.String(80))
    school_class = db.Column(db.String(80))
    school_grade = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Blog(db.Model):
    """
    ppt数据模型
    """

    # 主键ID
    id = db.Column(db.Integer, primary_key=True)
    # ppt标题
    title = db.Column(db.String(100))
    # ppt正文
    text = db.Column(db.Text)

    def __init__(self, title, text):
        """
        初始化方法
        """
        self.title = title
        self.text = text


# class TeacherWork(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), unique=True)
#     detail = db.Column(db.String(500))
#     answer = db.Column(db.String(5000))
#     course_id = db.Column(db.Integer)

#     def __init__(self, title, detail, answer, course_id):
#         self.title = title
#         self.detail = detail
#         self.answer = answer
#         self.course_id = course_id


# class StudentWork(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     userid = db.Column(db.Integer)
#     answer = db.Column(db.String(5000))
#     score = db.Column(db.DECIMAL(10, 2))
#     course_id = db.Column(db.Integer)

#     def __init__(self, userid, answer, score, course_id):
#         self.userid = userid
#         self.answer = answer
#         self.score = score
#         self.course_id = course_id


### -------------start of home
def replace_html_tag(text, word):
    new_word = '<font color="red">' + word + "</font>"
    len_w = len(word)
    len_t = len(text)
    for i in range(len_t - len_w, -1, -1):
        if text[i : i + len_w] == word:
            text = text[:i] + new_word + text[i + len_w :]
    return text


class PageResult:
    def __init__(self, data, page=1, number=2):
        self.__dict__ = dict(zip(["data", "page", "number"], [data, page, number]))
        self.full_listing = [
            self.data[i : i + number] for i in range(0, len(self.data), number)
        ]
        self.totalpage = len(data) // number
        print("totalpage=", self.totalpage)

    def __iter__(self):
        if self.page - 1 < len(self.full_listing):
            for i in self.full_listing[self.page - 1]:
                yield i
        else:
            return None

    def __repr__(self):  # used for page linking
        return "/home/{}".format(self.page + 1)  # view the next page


# 获取city对应列表
def read_city_kv():
    k_v = {}
    csv_file = "mydata/i0citycode_cityname.csv"
    with open(csv_file, "r", encoding="utf-8") as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = csv.reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            v, k = row[0].split("\t")
            # print(v,k)
            k_v[k] = v
    # print(k_v)
    return k_v


cityname_code = read_city_kv()

import time


def compare_time(time1, time2):
    s_time = time.mktime(time.strptime(time1, "%Y/%m/%d %H:%M:%S"))
    e_time = time.mktime(time.strptime(time2, "%Y/%m/%d %H:%M:%S"))
    # print 's_time is:',s_time
    # print 'e_time is:',e_time
    return int(s_time) - int(e_time)


# 出发机场,到达机场,航班编号,计划起飞时间,计划到达时间,实际起飞时间,实际到达时间,飞机编号,航班是否取消,需验证标识
def read_flight():
    mylist = []
    csv_file = "mydata/i1flight.csv"
    with open(csv_file, "r", encoding="utf-8") as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = csv.reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            # print(row)
            p3 = ""
            p4 = ""
            p5 = ""
            p6 = ""
            if row[3] != "":
                time_tuple_3 = time.localtime(int(row[3]))
                p3 = time.strftime("%Y/%m/%d %H:%M:%S", time_tuple_3)
                # print("北京时间：", t3)
            if row[4] != "":
                time_tuple_4 = time.localtime(int(row[4]))
                p4 = time.strftime("%Y/%m/%d %H:%M:%S", time_tuple_4)
            if row[5] != "":
                time_tuple_5 = time.localtime(int(row[5]))
                p5 = time.strftime("%Y/%m/%d %H:%M:%S", time_tuple_5)
            if row[6] != "":
                time_tuple_6 = time.localtime(int(row[6]))
                p6 = time.strftime("%Y/%m/%d %H:%M:%S", time_tuple_6)

            # result = compare_time(p3,'2017/06/25 00:00:00')
            # print('result', result)
            if p3 > "2017/06/25 10:00:00" and p3 < "2017/06/25 24:00:00":
                mylist.append([row[0], row[1], row[2], p3, p4, p5, p6, row[7]])
    return mylist


flights = read_flight()
print(len(flights), flights[:10])

history_whether_625 = {
    "上海": "小雨转雷阵雨,22,26,2017/6/25",
    "武汉": "阵雨转阴,23,30,2017/6/25",
    "北京": "多云,20,31,2017/6/25",
}


@app.route("/home/<int:pagenum>", methods=["GET"])
@app.route("/home", methods=["GET", "POST"])
def home(pagenum=1):
    global cityname_code, flights, history_whether_625
    print(cityname_code)
    print("home " * 10)
    keyword = ""
    blogs = Blog.query.all()
    user = None
    if "userid" in session:
        user = User.query.filter_by(id=session["userid"]).first()
    else:
        print("userid not in session")
    print("in home", user, "blogs=", len(blogs), "*" * 20)
    if request.method == "POST":
        search_list = []
        filter_flights = []
        # 查询对应城市的天气
        keyword = request.form["keyword"]
        print("keyword=", keyword, "@-@" * 10)
        if keyword is not None:

            # 实时api
            realtime_api = get_whether(keyword)
            print("realtime_api", "->", realtime_api)
            if realtime_api == "error":
                realtime_api = "晴朗"
            # citycode
            citycode = None
            if keyword in cityname_code:
                citycode = cityname_code[keyword]
                print("cityname_code=", citycode)
                for row in flights:
                    # [['PEK', 'CAN', 'CA1351', '2017/06/01 07:35:00', '2017/06/01 10:55:00', '', '', '2277']]
                    if row[0] == citycode:
                        filter_flights.append(row)
            print("filter_flights=", len(filter_flights), filter_flights[0:3])

        print("search_list=", search_list, "=>" * 5)
        # return rt("home.html", listing=PageResult(search_list, pagenum, 10), user=user, keyword=keyword,
        #         realtime_whether=keyword +'实时天气:'+'晴朗')
        msg = ""
        if keyword == "上海":
            msg = (
                "上海管制区航班延误黄色预警提示：6月26日上海管制区部分航路预计10:00至20:00受雷雨天气影响，通行能力下降30%左右。【空中交通网】"
            )
        return rt(
            "home.html",
            listing=None,
            user=user,
            keyword=keyword,
            realtime_whether=keyword + "realtime:" + realtime_api,
            filter_flights=filter_flights,
            old_whether=history_whether_625[keyword],
            msg=msg,
        )
        # return rt("home.html", listing=PageResult(search_list, pagenum, 2), user=user)

    return rt(
        "home.html",
        listing=PageResult(blogs, pagenum),
        user=user,
        realtime_whether=keyword + "realtime:sunny",
    )


@app.route("/blogs/create", methods=["GET", "POST"])
def create_blog():
    """
    创建ppt文章
    """
    if request.method == "GET":
        # 如果是GET请求，则渲染创建页面
        return rt("create_blog.html")
    else:
        # 从表单请求体中获取请求数据
        title = request.form["title"]
        text = request.form["text"]

        # 创建一个ppt对象
        blog = Blog(title=title, text=text)
        db.session.add(blog)
        # 必须提交才能生效
        db.session.commit()
        # 创建完成之后重定向到ppt列表页面
        return redirect("/blogs")


@app.route("/blogs", methods=["GET"])
def list_notes():
    """
    查询ppt列表
    """
    blogs = Blog.query.all()
    # 渲染ppt列表页面目标文件，传入blogs参数
    return rt("list_blogs.html", blogs=blogs)


@app.route("/blogs/update/<id>", methods=["GET", "POST"])
def update_note(id):
    """
    更新ppt
    """
    if request.method == "GET":
        # 根据ID查询ppt详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_blog.html", blog=blog)
    else:
        # 获取请求的ppt标题和正文
        title = request.form["title"]
        text = request.form["text"]

        # 更新ppt
        blog = Blog.query.filter_by(id=id).update({"title": title, "text": text})
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到ppt详情页面
        return redirect("/blogs/{id}".format(id=id))


@app.route("/blogs/<id>", methods=["GET", "DELETE"])
def query_note(id):
    """
    查询ppt详情、删除ppt
    """
    if request.method == "GET":
        # 到数据库查询ppt详情
        blog = Blog.query.filter_by(id=id).first_or_404()
        print(id, blog, "in query_blog", "@" * 20)
        # 渲染ppt详情页面
        return rt("query_blog.html", blog=blog)
    else:
        # 删除ppt
        blog = Blog.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


### -------------end of home
# @app.route("/recommend", methods=["GET", "DELETE"])
# def recommend():
#     """
#     查询ppt item 推荐
#     """
#     if request.method == "GET":
#         choosed = recommandation.main()
#         print("给予离线交互数据进行协同推荐")
#         print(choosed, "#" * 20)
#         print("给予离线交互数据进行协同推荐")
#         return rt("recommend.html", choosed=choosed)

### -------------start of profile


@app.route("/profile", methods=["GET", "DELETE"])
def query_profile():
    """
    查询ppt详情、删除ppt
    """

    id = session["userid"]

    if request.method == "GET":

        # 到数据库查询ppt详情
        user = User.query.filter_by(id=id).first_or_404()
        print(user.username, user.password, "#" * 5)
        # 渲染ppt详情页面
        return rt("profile.html", user=user)
    else:
        # 删除ppt
        user = User.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return "", 204


@app.route("/profiles/update/<id>", methods=["GET", "POST"])
def update_profile(id):
    """
    更新ppt
    """
    if request.method == "GET":
        # 根据ID查询ppt详情
        user = User.query.filter_by(id=id).first_or_404()
        # 渲染修改笔记页面HTML模板
        return rt("update_profile.html", user=user)
    else:
        # 获取请求的ppt标题和正文
        password = request.form["password"]
        nickname = request.form["nickname"]
        school_class = request.form["school_class"]
        school_grade = request.form["school_grade"]

        # 更新ppt
        user = User.query.filter_by(id=id).update(
            {
                "password": password,
                "nickname": nickname,
                "school_class": school_class,
                "school_grade": school_grade,
            }
        )
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到ppt详情页面
        return redirect("/profile")


### -------------end of profile


# @app.route("/course/<id>", methods=["GET"])
# def course_home(id):
#     """
#     查询ppt详情、删除ppt
#     """
#     if request.method == "GET":
#         # 到数据库查询ppt详情
#         blog = Blog.query.filter_by(id=id).first_or_404()
#         teacherWork = TeacherWork.query.filter_by(course_id=id).first()
#         print(id, blog, "in query_blog", "@" * 20)
#         # 渲染ppt详情页面
#         return rt("course.html", blog=blog, teacherWork=teacherWork)
#     else:
#         return "", 204


login_manager = flask_login.LoginManager(app)
user_pass = {}


# @app.route("/call_bash", methods=["GET"])
# def call_bash():
#     i0bash_caller.open_client("")
#     return {}, 200


@app.route("/statistics", methods=["GET"])
def relationship():
    # static/data/test_data.json
    filename = os.path.join(app.static_folder, "data.json")
    with open(filename) as test_file:
        d = json.load(test_file)
    print(type(d), "#" * 10, d)
    return jsonify(d)


@app.route("/index_a/")
def index():
    return rt("index-A.html")


@app.route("/index_b/")
def index_b():
    return rt("index-B.html")


@login_manager.user_loader
def load_user(email):
    print("$" * 30)
    return user_pass.get(email, None)


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        data = User.query.filter_by(username=email, password=password).first()
        print(data, "@" * 10)
        if data is not None:
            print("test login")
            session["logged_in"] = True

            if email in admin_list:
                session["isadmin"] = True
                print("@" * 20, "setting isadmin")
            session["userid"] = data.id

            print("login sucess", "#" * 20, session["logged_in"])

            # w = TeacherWork.query.get(1)
            # print('w=', w, w.answer, w.title)
            # if w is not None:
            #     session['title'] = w.title
            #     session['detail'] = w.detail
            #     session['answer'] = w.answer

            return redirect(url_for("home", pagenum=1))
        else:
            return "Not Login"
    except Exception as e:
        print(e)
        return "Not Login"
    return redirect(url_for("home", pagenum=1))


@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for("home", pagenum=1))
    # if DB.get_user(email):
    if email in user_pass:
        print("already existed user")
        return redirect(url_for("home", pagenum=1))
    # salt = PH.get_salt()
    # hashed = PH.get_hash(pw1 + salt)
    print("register", email, pw1)
    new_user = User(username=email, password=pw1)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("home", pagenum=1))


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return redirect(url_for("home", pagenum=1))


reviews = []


@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized"


# --------------------------
# @app.route("/add_ppt", methods=["GET"])
# def add_ppt():
#     return rt("index.html")


# @app.route("/upload_ppt", methods=["POST"])
# def upload_ppt():

#     # detail = request.form.get("detail")
#     # 从表单请求体中获取请求数据

#     title = request.form.get("title")
#     text = request.form.get("detail")

#     # 创建一个ppt对象
#     blog = Blog(title=title, text=text)
#     db.session.add(blog)
#     # 必须提交才能生效
#     db.session.commit()
#     # 创建完成之后重定向到ppt列表页面
#     # return redirect("/blogs")

#     return redirect(url_for("add_ppt"))


# @app.route("/student_work", methods=["POST"])
# def student_work():
#     return redirect(url_for("student_index"))


# @app.route("/student_index", methods=["GET"])
# def student_index():
#     return rt("student_index.html")


# @app.route("/", methods=["GET"])
# def index():
#     return rt("index.html")


@app.route("/file/upload", methods=["POST"])
def upload_part():  # 接收前端上传的一个分片
    task = request.form.get("task_id")  # 获取文件的唯一标识符
    chunk = request.form.get("chunk", 0)  # 获取该分片在所有分片中的序号
    filename = "%s%s" % (task, chunk)  # 构造该分片的唯一标识符
    print("filename=", filename)
    upload_file = request.files["file"]
    upload_file.save("./upload/%s" % filename)  # 保存分片到本地
    return rt("index.html")


@app.route("/file/merge", methods=["GET"])
def upload_success():  # 按序读出分片内容，并写入新文件
    global last_upload_filename
    target_filename = request.args.get("filename")  # 获取上传文件的文件名
    last_upload_filename = target_filename
    print("last_upload_filename=", last_upload_filename)
    task = request.args.get("task_id")  # 获取文件的唯一标识符
    chunk = 0  # 分片序号
    with open("./upload/%s" % target_filename, "wb") as target_file:  # 创建新文件
        while True:
            try:
                filename = "./upload/%s%d" % (task, chunk)
                source_file = open(filename, "rb")  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
            except IOError as msg:
                break

            chunk += 1
            os.remove(filename)  # 删除该分片，节约空间

    return rt("index.html")


@app.route("/file/list", methods=["GET"])
def file_list():
    files = os.listdir("./upload/")  # 获取文件目录
    # print(type(files))
    files.remove(".DS_Store")
    # files = map(lambda x: x if isinstance(x, unicode) else x.decode('utf-8'), files)  # 注意编码
    return rt("list.html", files=files)


@app.route("/file/download/<filename>", methods=["GET"])
def file_download(filename):
    def send_chunk():  # 流式读取
        store_path = "./upload/%s" % filename
        print("store_path=", store_path)
        with open(store_path, "rb") as target_file:
            while True:
                chunk = target_file.read(20 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(send_chunk(), content_type="application/octet-stream")


# Custom static data
@app.route("/cdn/<path:filename>")
def custom_static(filename):
    print("#" * 20, filename, " in custom_static", app.root_path)
    return send_from_directory(
        "/Users/abel/Downloads/AbelProject/FlaskRepository/ppt_platform/upload/",
        filename,
    )


# --------------------------


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="localhost", port=5000, threaded=False)
