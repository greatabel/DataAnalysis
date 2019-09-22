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

pairs = lines.map(lambda x: (x.split(" ")[0], len(x)))

# 在 Python 中使用第一个单词作为键创建出一个 pair RDD

for i in pairs.take(10):
    print(colored('i==>', 'red'), i)

# result = pairs.filter(lambda keyValue: keyValue[1] % 2 == 0 )
result = pairs.mapValues(lambda x: (x, 1))\
         .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

print('聚合操作')

for i in result.take(10):
    print(colored('i===>', 'green'), i)

