# --- 整体的流程 ----
我们的前后端主要基于：flask+sqlchemy + numpy+ html5+vue+jquery技术栈

对于科学数据集的管理：是flask 后端+ flask cros ,前端vue+bootstrap+ jinja 接受之后，传递到后端sqlchemy进行存储
大数据部分主要是echart+jquery+vue 经过数据集的分析，得出json三元组之后，然后和前端的ajax+js进行互动，可以进行拉伸和展示，进行各种主题直接的分析
挑选某一个特定数据集，专门进行大数据分析和探索，这部分主要是基于python3/spark/spark sql 进行的数据集探索，具体使用了sklearn进行机器学习相关模型构建

整体上主要是从前端Jinja的template页面触发事件，然后通过Flask API传递到pika中间件，pika然后传递到rabbitmq
Flask 是一个基于 Python 的轻量级 Web 框架，WSGI 工具箱采用 Werkzeug，模板引擎使用 Jinja2。由于其不依赖于特殊的工具或库，并且没有数据抽象层、表单验证或是其他任何已有多种库可以胜任的功能，从而保持核心简单、易于扩展，而被定义为"微"框架。但是，Flask 可以通过扩展来添加应用功能。并且 Flask 具有自带开发用服务器和 debugger、集成单元测试和 RESTful 请求调度 (request dispatching)、支持 secure cookie 的特点。我们就主要使用Flask的网站部分和wsgi写API部分




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

# -- 数据集简介 --- 
my_wheather_data.csv 是来自中国环境监测总站空气质量数据类型包括PM2.5, PM10, SO2, NO2, O3, CO, AQI等全国空气质量数据来自中国环境监测总站的全国城市空气质量实时发布平台，我们经过数据处理后的数据，
处理后得到"barometric_value","humidity","ultraviolet_rays","average_quality","ozone_relative","record_id","pm1","pm2","pm3","pm4" 相关的一些可供预测和分析的数据
参考： https://www.resdc.cn/data.aspx?DATAID=186

original 是天气和城市相关、机场相关的数据集，属于航空部门数据集
具体参考： https://www.heywhale.com/mw/dataset/59793a5a0d84640e9b2fedd3
https://www.payititi.com/opendatasets/show-25932.html
经过处理后变成了 i1fight.csv  my_wheater_data.csv



# ---  一些可能的疑问的解答 ----

1. 那个用户注册登陆是怎么实现的
具体你看structure_note.md 

一个实现密码哈希的包是Werkzeug，当安装Flask时，你可能会在pip的输出中看到这个包，因为它是Flask的一个核心依赖项。

管理用户登录状态，以便用户可以登录到应用，用户在导航到该应用的其他页面时，应用会“记得”该用户已经登录。
它还提供了“记住我”的功能，允许用户在关闭浏览器窗口后再次访问应用时保持登录状态

Flask-Login插件需要在用户模型上实现某些属性和方法。只要将这些必需项添加到模型中，
Flask-Login就可以与基于任何数据库系统的用户模型一起工作
这块是sqlchemy， 我们在i4wsgi.py里面有User class

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

用户会话是Flask分配给每个连接到应用的用户的存储空间，Flask-Login通过在用户会话中存储其唯一标识符（ID）来跟踪登录用户。每当已登录的用户导航到新页面时，Flask-Login将从会话中检索用户的ID，然后将该用户实例加载到内存中。此时，相当于Login插件已知用户ID，需要返回具体用户，因此插件期望应用配置一个用户加载函数，可以调用该函数来加载给定ID的用户

需要一个HTML模板以便在网页上显示这个表单，存储在moive/templates/home.html文件里

2. 把脏数据过滤掉，根据相关性热图删掉了后面几列数据
这个在mydata/my_wheather_data.csv获得数据前进行过一次错误或者不全的数据过滤了
至于你说的相关性热图删掉了后面几列数据，则是根据数据规律和常识了。
affinity analysis ----------------------------------------这个图里面完全没有规律的，肯定是不需要的；
而根据常识，想record_id 这个肯定也是不需要的，因为和数据趋势没啥关系，这是数据集的标识