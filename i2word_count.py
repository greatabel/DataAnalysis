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

rdd = sc.textFile("log.txt")

words = rdd.flatMap(lambda x: x.split(" "))

# 在 Python 中使用第一个单词作为键创建出一个 pair RDD

for i in words.take(10):
    print(colored('i==>', 'red'), i)

# result = pairs.filter(lambda keyValue: keyValue[1] % 2 == 0 )
result = words.map(lambda x: (x, 1))\
         .reduceByKey(lambda x, y: x+y)


print(colored('用 Python 实现单词计数', 'blue'))
for i in result.take(10):
    print(colored('i===>', 'green'), i)

