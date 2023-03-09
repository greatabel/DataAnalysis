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
python3 i1wsgi.py



6.
浏览器访问：

访问不同的用户，比如用户user 101
http://localhost:5000/index_a?id=101
访问不同的用户，比如用户user 102
http://localhost:5000/index_a?id=102


知识图谱的示例json文件放在：movie/static/kg_data下面的：
data_1.json
data_1.json
...
买家可以根据例子，增加和生成自己的json
