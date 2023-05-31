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

4.2
python3 -m spacy download zh_core_web_sm

4.3
python3 i0data_extractor.py

5.
模拟运行在:
python3 i2wsgi.py




6.

浏览器访问 首页在：
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

1. 这里才3k条，做可视化用下json+flask+d3就可以了
2. 数据买家提供了573条，需要抽取至少2000三元组（我们估计会使用Causality抽取，Sequentia抽取等等方法选择最好的方法），
	应该不需要gpu，cpu足够


# ------------------------------ end 总需求 ------------------------------------





