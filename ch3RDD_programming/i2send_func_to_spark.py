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

# 遍历结果
# errorsRDD = inputRDD.filter(lambda line: "error" in line)
def containsError(s):
    return 'error' in s

word = inputRDD.filter(containsError)

for i in word.take(10):
    print(colored('i==>', 'red'), i)
