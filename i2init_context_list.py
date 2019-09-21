'''

https://stackoverflow.com/questions/36708338/pyspark-pipelinedrdd-object-is-not-iterable

'''

import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from termcolor import colored

'''
sparkcontext 需要2个参数：
集群URL： 告诉spark如何连接到集群。 这里我们使用的是local，告诉spark运行在单机
线程上而无需连接到集群

应用名： 例子是：PySparkShell 当连接到一个集群，这个值可以帮助你在集群管理器中
的用户界面中找到你的应用

'''
conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")
# spark = SQLContext(sc)

#创建一个lines的RDD
lines = sc.textFile("i1introduction.md")

# 遍历结果
sparklines = lines.filter(lambda line: "Spark" in line)
for i in sparklines.collect():
    print(colored('i==>', 'red'), i)