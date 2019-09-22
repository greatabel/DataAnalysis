import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from termcolor import colored


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")
# spark = SQLContext(sc)

lines = sc.parallelize(["I am abel", "hi", "Hello world", 
                        "xiaoming, how are your?", "I am fine!"])

words = lines.map(lambda x: (x.split(" ")[0], len(x)))
# 在 Python 中使用第一个单词作为键创建出一个 pair RDD

for i in words.take(10):
    print(colored('i==>', 'red'), i)

sumCount = words.combineByKey((lambda x: (x,1)),
                             (lambda x, y: (x[0] + y, x[1] + 1)),
                             (lambda x, y: (x[0] + y[0], x[1] + y[1])))
# https://github.com/databricks/learning-spark/issues/24
r = sumCount.map(lambda kvp: ( kvp[0], kvp[1][0] / kvp[1][1] ) ).collectAsMap()




print(colored('平均值', 'blue'))
for i in r:
    print(colored('i===>', 'green'), i)

