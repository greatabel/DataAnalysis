import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from termcolor import colored
import json
import re


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")
# spark = SQLContext(sc)



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
# callSigns.saveAsTextFile(outputDir + "/callsigns")
print("Blank lines: %d" % blankLines.value)

# 创建用来验证呼号的累加器
validSignCount = sc.accumulator(0)
invalidSignCount = sc.accumulator(0)

def validateSign(sign):
    global validSignCount, invalidSignCount
    if re.match(r"\A\d?[a-zA-Z]{1,2}\d{1,4}[a-zA-Z]{1,3}\Z", sign):
        validSignCount += 1
        return True
    else:
        invalidSignCount += 1
        return False

# 对与每个呼号的联系次数进行计数
validSigns = callSigns.filter(validateSign)
contactCount = validSigns.map(
    lambda sign: (sign, 1)).reduceByKey((lambda x, y: x + y))

# 强制求值计算计数
contactCount.count()
if invalidSignCount.value < 0.1 * validSignCount.value:
    contactCount.saveAsTextFile(outputDir + "/contactCount")
else:
    print("Too many errors: %d in %d" % (invalidSignCount.value, validSignCount.value) )




