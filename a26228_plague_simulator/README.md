1.
安装python3.6 以上版本

2. 
安装pip3 
（如果网速慢 可以pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  把some-package替换成自己的慢的包 )

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
模拟运行在:
python3 i2wsgi.py




6.
浏览器访问：
http://localhost:5000/mysimulation

首页在：
http://localhost:5000/home


已经注册好的管理员账号 可以直接登录：
管理员1
username: greatabel1@126.com
password: abel
你也可以自己注册和登录


-------------------
一般用户测试账号:(geust_test)
username:test@126.com
password: test

7.
个人主页： http://localhost:5000/profile









# ------------------------------ 总需求 ------------------------------------

我们也不能和《瘟疫2》截图完全一样，他是flash开发的，flash已经没人用了。
我们可以给予Flask/boostrap/vue/d3/numpy/siencekit等实现：

Flask：Python 的轻量级 Web 框架，用于构建后端服务，处理模拟请求和返回模拟结果。
Leaflet.js：一个开源的 JavaScript 地图库，用于在前端显示交互式地图。
HTML、CSS 和 JavaScript：用于构建和样式化前端界面，以及处理用户交互和显示模拟结果。
实现的功能：


1.
设计基本的传播模型

确定传播模型的基本参数，例如感染率、恢复率、潜伏期等。
为不同类型的流行病定义特征和传播方式，例如空气传播、飞沫传播等。
考虑其他因素：

2。
设计模型因素
添加人口密度、医疗资源等因素，并将其纳入传播模型。
创建不同的场景设置选项，让用户可以调整模拟环境。
构建 Flask 后端：

3.
web api：
创建一个 Flask 应用，并为其添加路由以处理前端发起的请求。
编写一个用于运行模拟的函数。该函数根据输入参数（例如病原体类型、场景设置等）执行模拟，并返回预测结果。
通过 Flask 的 API 路由，将运行模拟的函数与前端连接。

4.
构建前端界面：

使用 HTML5/CSS/boostrap/vue 设计一个简单的界面，包括用于选择病原体类型、场景设置的下拉菜单，以及显示模拟结果的图表。
使用 VUe和开源地图 为界面添加交互功能，例如在用户选择不同参数时，向 Flask 后端发起请求并获取预测结果。
预测和策略建议

5.
模拟功能：
根据模拟结果，为用户提供建议
用户可以通过下拉列表选择不同的流行病、场景和应对策略。

6. 可视化：
6.1
用户可以点击“模拟”按钮以运行模拟。模拟请求将发送到 Flask 后端，后端将根据用户选择的参数计算模拟结果并返回。
模拟结果显示在前端页面上。
地图显示了传播点和传播路线，以及一些主要国际机场的位置。每次运行模拟时，传播点和路线会根据后端返回的数据更新。
用户可以查看地图上的传播点、传播路线和机场信息。

6.2
感染数量直接显示出到地图上，通过小旗子或者其他图标标出数量等，尽量地图上的表现形式再多一点



# ------------------------------ end 总需求 ------------------------------------




