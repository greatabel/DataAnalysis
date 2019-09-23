import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from termcolor import colored
import json

conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")
# spark = SQLContext(sc)

lines = sc.parallelize(["I am abel", "hi abel", "Hello world", "xiaoming, how are your?"])

inputFile = 'input_demo.txt'
outputDir = 'i0out.txt'
file = sc.textFile(inputFile)
# 创建Accumulator[Int]并初始化为0
blankLines = sc.accumulator(0)

def extractCallSigns(line):
    global blankLines # 访问全局变量
    if (line == ""):
        blankLines += 1
    return line.split(" ")

callSigns = file.flatMap(extractCallSigns)
callSigns.saveAsTextFile(outputDir + "/callsigns")
print("Blank lines: %d" % blankLines.value)



