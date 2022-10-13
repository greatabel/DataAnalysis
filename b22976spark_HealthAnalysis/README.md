1.
安装python3.6 以上版本

2. 
安装pip3 

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
开启命令行运行，运行：
jupyter notebook i1spark_ml.ipynb
(因为我已经缓存了所有的机器学习训练过程和结果，买家可以不需要重新训练，买家可以不用配置pyspark
既可以打开工程，查看结果)

6.
浏览器访问：http://localhost:8888/notebooks/i1spark_ml.ipynb

7.
（可选)
pip install --upgrade -r full_requirements.txt
买家需要重新训练时候，才需要配置本地spark环境和变量，然后重新从头到尾执行i1saprk_ml.ipynb,
只是查看是不需要执行



