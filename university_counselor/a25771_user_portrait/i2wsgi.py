"""App entry point."""
import os
import sys
import json
import random
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
from flask import make_response

# from flask_wtf.csrf import CSRFProtect
from flask import flash

from movie import create_app

# import es_search
import logging
from os import listdir

# 大屏可视化
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

# 可视化用户画像
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
import pandas as pd
from pyspark.ml.clustering import KMeans

# 获取已安装字体的路径
font_path = 'SourceHanSansCN-Regular.otf'

# 创建字体属性对象
font = FontProperties(fname=font_path)
import warnings
warnings.filterwarnings("ignore", category=UserWarning)





app = create_app()
app.secret_key = "ABCabc123"
app.debug = True


handler = logging.FileHandler("flask.log", encoding="UTF-8")
handler.setLevel(
    logging.DEBUG
)  # 设置日志记录最低级别为DEBUG，低于DEBUG级别的日志记录会被忽略，不设置setLevel()则默认为NOTSET级别。
logging_format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s"
)
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


CORS(app)

# 防御点3: CSRF攻击模拟 防御
# CSRFProtect(app)

# --- total requirement ----


# ---start  数据库 ---

print("#" * 20, os.path.abspath("movie/campus_data.db"), "#" * 20)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(
    "movie/campus_data.db"
)
# 防御点1: 防止入sql-inject ，不实用sql注入，sqlchemy让代码ORM化，安全执行
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
    def __init__(self, data, page=1, number=4):
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


@app.route("/home/<int:pagenum>", methods=["GET"])
@app.route("/home", methods=["GET", "POST"])
def home(pagenum=1):
    print("home " * 10)
    app.logger.info("home info log")

    blogs = Blog.query.all()
    blogs = list(reversed(blogs))
    user = None
    if "userid" in session:
        user = User.query.filter_by(id=session["userid"]).first()
    else:
        print("userid not in session")
    print("in home", user, "blogs=", len(blogs), "*" * 20)
    if request.method == "POST":
        search_list = []
        keyword = request.form["keyword"]
        print("keyword=", keyword, "-" * 10)
        if keyword is not None:
            for blog in blogs:
                if keyword in blog.title or keyword in blog.text:
                    blog.title = replace_html_tag(blog.title, keyword)
                    print(blog.title)
                    blog.text = replace_html_tag(blog.text, keyword)

                    search_list.append(blog)


        print("search_list=", search_list, "=>" * 5)
        return rt(
            "home.html",
            listing=PageResult(search_list, pagenum, 10),
            user=user,
            keyword=keyword,
        )
        # return rt("home.html", listing=PageResult(search_list, pagenum, 2), user=user)

    return rt("home.html", listing=PageResult(blogs, pagenum), user=user)


@app.route("/blogs/create", methods=["GET", "POST"])
def create_blog():
    """
    创建商品
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





### -------------end of home
with open("user_recommendations_filtered.json", "r") as f:
    user_recs_dict = [json.loads(line) for line in f]


def get_recommendations(user_id):
    recommendations = [rec for rec in user_recs_dict if rec["userId"] == user_id]
    if not recommendations:
        return None
    return recommendations


def generate_random_recs(user_id, num_recs=4):
    random_recs = []
    item_categories = ['Ecommerce_categoryA(娱乐)', 'Ecommerce_categoryB(娱乐)']
    generated_item_ids = set()

    while len(random_recs) < num_recs:
        item_id = random.randint(1, 10)  # 假设最大的itemId为10
        if item_id not in generated_item_ids:
            generated_item_ids.add(item_id)
            random_recs.append({
                "itemId": item_id,
                "userId": user_id,  # 使用传入的user_id
                "rating": round(random.uniform(1, 5), 2),  # 生成一个1到5之间的随机评分
                "itemName": "room"+str(item_id),  # 您可以根据实际情况填写这些字段
                "itemCategory": random.choice(item_categories)  # 随机选择一个分类
            })

    return random_recs



@app.route("/recommend", methods=["GET", "DELETE"])
def recommend():
    """
    查询商品 item 推荐
    """
    if request.method == "GET":
        id = session["userid"]
        print(id, "#" * 20, "in recommend")
        recs = get_recommendations(id)
        if recs:
            print("recs=", recs)
        else:
            recs = generate_random_recs(id)
        # Get the list of image filenames in the recommends folder
        image_files = [f for f in listdir('movie/static/images/ppt_cover/recommends') if f.endswith('.jpg')]

        return rt("recommend.html", choosed=recs, image_files=image_files)


### -------------start of visualization bigscreen


@app.route("/plot")
def plot():
    # 创建SparkSession
    spark = SparkSession.builder.appName("UserPortrait").getOrCreate()

    # 加载用户数据
    user_df = spark.read.csv("data/user_data.csv", header=True, inferSchema=True)

    # 加载用户行为数据
    behavior_df = spark.read.csv("data/user_behavior_data.csv", header=True, inferSchema=True)



    # In[6]:


    # 统计用户数据中的记录数量
    user_count = user_df.count()

    # 统计用户行为数据中的记录数量
    behavior_count = behavior_df.count()

    # 打印结果
    print("用户数据中的记录数量：", user_count)
    print("用户行为数据中的记录数量：", behavior_count)


    # In[7]:


    # 计算用户数据中各特征之间的相关系数
    # Convert the Spark DataFrame to a Pandas DataFrame
    user_df_pd = user_df.toPandas()

    # 将性别从分类变量转换为数值变量
    user_df_pd['gender_numeric'] = user_df_pd['gender'].map({'Male': 0, 'Female': 1})

    # 重新计算相关性矩阵
    corr_matrix = user_df_pd.corr()
    
    # 将相关矩阵转换为 JSON，以便在模板中使用
    corr_matrix_json = corr_matrix.to_json(orient="split")
    print('#'*30, corr_matrix_json)
    
    # 计算年龄分布直方图数据
    age_histogram_data = user_df_pd['age'].value_counts().reset_index()
    age_histogram_data.columns = ['age', 'count']
    age_histogram_json = age_histogram_data.to_json(orient="records")

    # 将数据添加到模板


    # 计算性别分布柱状图数据
    gender_count_data = user_df_pd['gender'].value_counts().reset_index()
    gender_count_data.columns = ['gender', 'count']
    gender_count_json = gender_count_data.to_json(orient="records")
    
    behavior_df_pd = behavior_df.toPandas()
    # 计算年龄与评分关系散点图数据
    user_behavior_df_pd = pd.merge(user_df_pd, behavior_df_pd, on="userId")
    age_rating_scatter_data = user_behavior_df_pd[["age", "rating", "gender"]]
    age_rating_scatter_json = age_rating_scatter_data.to_json(orient="records")

    # 将数据添加到模板
    return rt("plot.html", corr_matrix=corr_matrix_json, 
        age_histogram=age_histogram_json, gender_count=gender_count_json, age_rating_scatter=age_rating_scatter_json)



### -------------end of visualization bigscreen



@app.route("/profile", methods=["GET", "DELETE"])
def query_profile():
    """
    查询商品详情、删除ppt
    """

    id = session["userid"]

    if request.method == "GET":

        # 到数据库查询ppt详情
        user = User.query.filter_by(id=id).first_or_404()
        print(user.username, user.password, "#" * 5)
        # 渲染ppt详情页面
        r = make_response(rt("profile.html", user=user))
        # 防御点2：xss攻击，实用csp方式： https://content-security-policy.com/
        r.headers.set(
            "Content-Security-Policy",
            "default-src * 'unsafe-inline'; connect-src 'self' 'nonce-987654321' ",
        )
        return r
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





login_manager = flask_login.LoginManager(app)
user_pass = {}





@app.route("/statistics", methods=["GET"])
def relationship():
    # static/data/test_data.json
    filename = os.path.join(app.static_folder, "data.json")
    # with open(filename) as test_file:
    with open(filename, "r", encoding="utf-8") as test_file:
        d = json.load(test_file)
    print(type(d), "#" * 10, d)
    return jsonify(d)




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
    data = User.query.filter_by(username=email).first()
    # if email in user_pass:
    if data is not None:
        print("already existed user")
        flash("already existed user")
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
@app.route("/add_ppt", methods=["GET"])
def add_ppt():
    return rt("index.html")


@app.route("/upload_ppt", methods=["POST"])
def upload_ppt():

    # detail = request.form.get("detail")
    # 从表单请求体中获取请求数据

    title = request.form.get("title")
    text = request.form.get("detail")

    # 创建一个ppt对象
    blog = Blog(title=title, text=text)
    db.session.add(blog)
    # 必须提交才能生效
    db.session.commit()
    # 创建完成之后重定向到ppt列表页面
    # return redirect("/blogs")

    return redirect(url_for("add_ppt"))




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
