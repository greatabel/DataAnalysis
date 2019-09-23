import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from termcolor import colored
from pyspark.sql import HiveContext


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")

hiveCtx = HiveContext(sc)
tweets = hiveCtx.read.json('demo.json')
tweets.registerTempTable('tweets')
results = hiveCtx.sql("select name from tweets")

for i in results.take(10):
    print(colored('i==>', 'red'), i)



