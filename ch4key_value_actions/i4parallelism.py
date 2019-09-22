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
data = [("a", 3), ("b", 4), ("a", 7), ("C", 10), ("b", 6)]
#默认并行度
lines = sc.parallelize(data).reduceByKey(lambda x, y: x+y)

lines_self = sc.parallelize(data).reduceByKey(lambda x, y: x+y, 10)
# 在 Python 中使用第一个单词作为键创建出一个 pair RDD

for i in lines_self.take(10):
    print(colored('i==>', 'red'), i)

print('--在 Python 中以字符串顺序对整数进行自定义排序--')
data_a = ['100', '200', '5', '30']
rdd = sc.parallelize(data_a)
r = rdd.sortByKey(ascending=True, numPartitions=None, keyfunc = lambda x: x).collect()

for i in r:
    print(colored('i===>', 'green'), i)

