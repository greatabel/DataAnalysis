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

lines = sc.parallelize(["I am abel", "hi", "Hello world", "xiaoming, how are your?"])

pairs = lines.map(lambda x: (x.split(" ")[0], x))

# 在 Python 中使用第一个单词作为键创建出一个 pair RDD

for i in pairs.take(10):
    print(colored('i==>', 'red'), i)

result = pairs.filter(lambda keyValue: len(keyValue[1]) < 10)

for i in result.take(10):
    print(colored('i==>', 'green'), i)

