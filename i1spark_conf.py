import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from termcolor import colored
import json

# conf = SparkConf().setMaster('local').setAppName('PySparkShell')
# 创建一个conf对象
conf = SparkConf()
conf.set("spark.app.name", "My Spark App")
conf.set("spark.master", "local[4]")
conf.set("spark.ui.port", "36000") # 重载默认端口配置


sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")