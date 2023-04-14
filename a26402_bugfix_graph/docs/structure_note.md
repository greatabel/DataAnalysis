# --- 整体的流程 ----
我们的前后端主要基于：flask+sqlchemy + numpy+ html5+vue+jquery技术栈

对于共同学习材料的管理：是flask 后端+ flask cros ,前端vue+bootstrap+ jinja 接受之后，传递到后端sqlchemy进行存储
数据前端部分主要是echart+jquery+vue 



整体上主要是从前端Jinja的template页面触发事件，然后通过Flask API传递到pika中间件，pika然后传递到rabbitmq
Flask 是一个基于 Python 的轻量级 Web 框架，WSGI 工具箱采用 Werkzeug，模板引擎使用 Jinja2。由于其不依赖于特殊的工具或库，并且没有数据抽象层、表单验证或是其他任何已有多种库可以胜任的功能，从而保持核心简单、易于扩展，而被定义为"微"框架。但是，Flask 可以通过扩展来添加应用功能。并且 Flask 具有自带开发用服务器和 debugger、集成单元测试和 RESTful 请求调度 (request dispatching)、支持 secure cookie 的特点。我们就主要使用Flask的网站部分和wsgi写API部分

主要的请求流程是这样：
Flask从请求到响应的流程:
客户端-----> wsgi server ----> 通过call调用 wsgi_app, 生成requests对象和上下文环境------> full_dispatch_request功能 ---->通过 dispatch_requests进行url到view function的逻辑转发, 并取得返回值 ------> 通过make_response函数,将一个view_function的返回值转换成一个response_class对象------->通过向response对象传入environ和start_response参数, 将最终响应返回给服务器--->
返回给前端的html的页面或者form ---》 用户看到实际ui的变化



# --- 分个介绍 ----

Jinja2 是基于 Python 的模版引擎，支持 Unicode，具有集成的沙箱执行环境并支持选择自动转义。Jinja2 拥有强大的自动 HTML 转移系统，可以有效的阻止跨站脚本攻击；通过模版继承机制，对所有模版使用相似布局；通过在第一次加载时将源码转化为 Python 字节码从而加快模版执行时间。我们的网站看得到的页面部分是这块开发。

Flask
1、Flask主要包括Werkzeug和Jinja2两个核心函数库，他们分别负责阢处理和安全方面的工鞥呢，这些基础函数为Web项目开发过程提供了丰富的基础组件。
　　2、Flask中的Jinja2模板引擎，提高了前端代码的复用率。可以大大提高开发效率并且有利于后期的开发与维护。
　　3、Flask不会指定数据库和模板引擎等对象，用户可以根据需要自己选择各种数据库。
　　4、Flask不提供表单验证功能，在项目实施过程中可以自由配置，从而为应用程序开发提供数据库抽象层基础组件，支持进行表单数据合法性验证、文件上传处理、用户身份认证和数据库集成等功能。
    Flask的特点可以概括为：因为灵活，轻便高效，被业界所认可，同时拥有基于Werkzeug、Jinja2等一些开源库，拥有内置服务器和单元测试，适配RESTful。我们使用flask编写网站的用户登录/注册/权限管理/个人主页/机器学习训练和可视化的前后台逻辑部分，非常方便后续进行扩展。
我将使用 SQLite，这是一个小型 SQL 数据库实现，非常容易启动和运行。请记住，您可能想在生产环境中考虑更可靠的数据库，例如 PostgreSQL 或 MySQL。

flask_sqlalchemy
要在 Flask 项目中设置 SQLAlchemy，我们可以导入 flask_sqlalchemy 软件包（我们之前已安装），然后将 Flask app 变量包装在新的 SQLAlchemy 对象。我们还希望在 Flask 应用程序配置中设置 SQLALCHEMY_DATABASE_URI 以指定我们要使用的数据库以及如何访问它

# -- 基于数据库添加

Flask-SQLAlchemy 是一个 Flask 扩展，用于简化在 Flask 应用中使用 SQLAlchemy 的过程。它提供了一个高层次的封装，使得在 Flask 应用中使用 SQLAlchemy 变得更加方便。
Flask-SQLAlchemy 使用了 SQLAlchemy 的核心功能，包括数据库会话和对象关系映射 (ORM)，并将其集成到 Flask 应用中。
在 Flask-SQLAlchemy 中，所有的数据库操作都使用会话 (Session) 来执行。会话用于将对象加载到内存中，并将对象的修改持久化到数据库中。
Flask-SQLAlchemy 也提供了一个高层次的 ORM，允许你使用 Python 类来映射数据库表。这些类被称为模型 (Model)，并使用 SQLAlchemy 的 declarative API 来定义。
模型类中的每个属性都映射到数据库表中的一个字段。使用 Flask-SQLAlchemy 的 ORM，可以使用 Python 代码而不是 SQL 语句来查询、插入、更新和删除数据库中的数据。

Flask-SQLAlchemy 提供了一种简单、方便的方式在 Flask 应用中使用 SQLAlchemy，使得你可以使用 Python 代码而不是 SQL 语句来操作数据库。
创建一个 SQLAlchemy 实例，并将其绑定到你的 Flask 应用：

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus_data.db"
db = SQLAlchemy(app)


可以使用以下代码来定义用户、博客（也就是学习资料的介绍实体）和评论模型
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

剩下的会是（这部分还没有设计在flask_sqlchemy中创建）：
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

在上面的代码中，我们使用了SQLAlchemy的多对多关系来表示用户，学习材料和评论之间的关系


# -- api 风格--- 
最后，我们可以开始定义 RESTful 处理程序。我们将使用 Flask-RESTful 软件包，这是一组工具，可帮助我们使用面向对象的设计来构建 RESTful 路由。

REST架构风格
六条设计规范定义了一个 REST 系统的特点:
客户端-服务器: 客户端和服务器之间隔离，服务器提供服务，客户端进行消费。
无状态: 从客户端到服务器的每个请求都必须包含理解请求所必需的信息。换句话说， 服务器不会存储客户端上一次请求的信息用来给下一次使用。
可缓存: 服务器必须明示客户端请求能否缓存。
分层系统: 客户端和服务器之间的通信应该以一种标准的方式，就是中间层代替服务器做出响应的时候，客户端不需要做任何变动。
统一的接口: 服务器和客户端的通信方法必须是统一的。
按需编码: 服务器可以提供可执行代码或脚本，为客户端在它们的环境中执行。这个约束是唯一一个是可选的。

Flask-RESTful
我们需要设置 Flask-RESTful 扩展名才能在 Flask 服务器中启动并运行。Flask-RESTful 是一个 Flask 扩展，它添加了快速构建 REST APIs 的支持。它当然也是一个能够跟你现有的ORM/库协同工作的轻量级的扩展。Flask-RESTful 鼓励以最小设置的最佳实践

Vue
整个平台的前端部分和可视化部分我们主要是使用vue+jquery+html5: Vue 是一套用于构建用户界面的渐进式 JavaScript 框架 ；同时它是一个典型的 MVVM 模型的框架（即：视图层-视图模型层-模型层）;HTML5是HTML的新标准，是一种超文本标记语言，是用来创建网页的标准标记语言，通过一系列的标识，来规范网络上的文档格式;区别：
        1.vue是一个渐进式 JavaScript 框架，而HTML5是一种超文本标记语言  2.在开发中vue框架通过mvvm的模式，解耦了视图层与模型层，而HTML5原生开中数据与标签紧耦合；    但是vue和html5可以进行结合:    vue是一个前端框架，但还是建立在HTML ，CSS ，JavaScript的基础之上的，通过编译之后依然是HTML+CSS+JavaScript组成。




