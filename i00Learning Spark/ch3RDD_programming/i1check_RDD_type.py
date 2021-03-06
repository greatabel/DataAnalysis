
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

#创建一个lines的RDD
inputRDD = sc.textFile('log.txt')
print('inputRDD类型:', inputRDD, isinstance(inputRDD, RDD))
# 遍历结果
errorsRDD = inputRDD.filter(lambda line: "error" in line)
print('errorsRDD类型:', errorsRDD, isinstance(errorsRDD, RDD))
# print(colored('把RDD持久化到内存中', 'red'))
# pandaslines.persist( StorageLevel.MEMORY_AND_DISK_2 )
# print('getStorageLevel=', pandaslines.getStorageLevel())

for i in errorsRDD.collect():
    print(colored('i==>', 'red'), i)

print('-'*30)
warningRDD = inputRDD.filter(lambda x: 'warning' in x)
badLinesRDD = errorsRDD.union(warningRDD)
for i in badLinesRDD.collect():
    print(colored('i==>', 'blue'), i)

print(colored('行动操作', 'green'))
c = 'input had ' + str(badLinesRDD.count()) + ' concerning lines'
print(c, ' Here are 10 exmamples:')
for line in badLinesRDD.take(10):
    print(line)