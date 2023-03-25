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

新开一个cmd：
jupyter notebook i2gps_algroithm_spark.ipynb



6.
浏览器访问：

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






# ------ 总需求 ------

1. 我们就生成数据集
生成用户数据集
生成用户行为数据集（都是大量的）
数据是模拟用户的“sql脚本”进行修改的

2.

接下来，我们加载两个数据集：用户数据和用户行为数据。我们使用Spark读取CSV文件，
并在读取时指定数据中包含的列名和数据类型。(csv可以从hadoop读取，可以从文件系统)


3.
训练一个基于ALS算法的推荐模型，用于为每个用户生成多个推荐商品（商品可以换成房间）。

4.
加载并可视化用户数据：从CSV文件加载用户数据，使用seaborn库绘制用户年龄分布图和地理位置云图。

5.
5.1
训练XGBoost分类器：将用户特征向量和标签转换为Spark数据类型，并将其拆分为训练集和测试集。
5.2
使用GBT分类器训练模型，并使用测试集评估其性能。
5.3
可视化混淆矩阵和计算Jaccard相似度：从GBT预测结果中生成混淆矩阵，计算Jaccard相似度，
并使用matplotlib库绘制可视化的混淆矩阵

6.
6.1
在spark中使用KMeans算法对用户进行聚类
6.2
添加聚类标签到用户画像数据中
6.3
将聚类标签连接到推荐结果数据中

7.
用户画像和推荐结果连接起来，并将S使用Seaborn库绘制了用户年龄分布图和用户地理位置云图。

8.
创建特征列和标签列，并使用逻辑回归算法计算用户标签。这样，我们就可以使用用户画像和推荐结果为新用户生成标签。

9.
弄一个网站的数据可视化页面，可视化方式展示
我们显示了用户画像、推荐结果和标签结果。

使用Flask创建一个Web应用程序，该应用程序将显示可视化结果。

使用Vue框架编写前端页面，向后端发送HTTP请求获取数据，并使用ECharts库在页面上呈现数据。
在页面上显示用户年龄分布图、用户地理位置云图和推荐结果。

10.
使用Flask提供REST API，使用户可以将新用户的数据输入到系统中，然后根据这个新用户生成推荐结果和标签，最后将结果返回给用户

11.
easearch的 docker部署和 flask的联调（可选


# ------ end 总需求 ------





