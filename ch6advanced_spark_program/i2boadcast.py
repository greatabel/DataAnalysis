import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark import SparkFiles
from pyspark.rdd import RDD
from termcolor import colored
import json
import re
import bisect
import os
import urllib3


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")
# spark = SQLContext(sc)



inputFile = 'input_demo.txt'
outputDir = 'i0out'

import shutil
if os.path.isdir(outputDir):
    shutil.rmtree(outputDir)

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

#----- boacast ----------#
def lookupCountry(sign, prefixes):
    pos = bisect.bisect_left(prefixes, sign)
    return prefixes[pos].split(",")[1]


def loadCallSignTable():
    f = open("callsign_tbl_sorted", "r")
    return f.readlines()


# 读取为国家代码来进行查询
# signPrefixes = loadCallSignTable()

# prefixes to country code to support this lookup.


# def processSignCount(sign_count, signPrefixes):
#     country = lookupCountry(sign_count[0], signPrefixes)
#     count = sign_count[1]
#     return (country, count)
signPrefixes = sc.broadcast(loadCallSignTable())

def processSignCount(sign_count, signPrefixes):
    country = lookupCountry(sign_count[0], signPrefixes.value)
    count = sign_count[1]
    return (country, count)

countryContactCounts = (contactCount
                        .map(lambda signCount: processSignCount(signCount, signPrefixes))
                        .reduceByKey((lambda x, y: x + y)))

countryContactCounts.saveAsTextFile(outputDir + "/countries.txt")

#-----基于分区进行操作----

# Query 73s for the call signs CallLogs and parse the personse


def processCallSigns(signs):
    """Lookup call signs using a connection pool"""
    # Create a connection pool
    http = urllib3.PoolManager()
    # the URL associated with each call sign record
    urls = map(lambda x: "http://73s.com/qsos/%s.json" % x, signs)
    # create the requests (non-blocking)
    requests = map(lambda x: (x, http.request('GET', x)), urls)
    # fetch the results
    result = map(lambda x: (x[0], json.loads(x[1].data)), requests)
    # remove any empty results and return
    return filter(lambda x: x[1] is not None, result)


def fetchCallSigns(input):
    """Fetch call signs"""
    # 使用 mapPartitions 函数获得输入 RDD 的每个分区中的元素迭代器，
    # 而需要返回的是执行结果的序列的迭代器。
    return input.mapPartitions(lambda callSigns: processCallSigns(callSigns))

contactsContactList = fetchCallSigns(validSigns)


#--------- 调用外部R ------------------

# Compute the distance of each call using an external R program
distScript = os.getcwd()+"/finddistance.R"
print('distScript=', distScript)
distScriptName = "finddistance.R"
sc.addFile(distScript)


def hasDistInfo(call):
    """Verify that a call has the fields required to compute the distance"""
    requiredFields = ["mylat", "mylong", "contactlat", "contactlong"]
    return all(map(lambda f: call[f], requiredFields))


def formatCall(call):
    """Format a call so that it can be parsed by our R program"""
    return "{0},{1},{2},{3}".format(
        call["mylat"], call["mylong"],
        call["contactlat"], call["contactlong"])

# pipeInputs = contactsContactList.values().flatMap(
#     lambda calls: map(formatCall, filter(hasDistInfo, calls)))
# distances = pipeInputs.pipe(SparkFiles.get(distScriptName))
# print('distances.collect()=', distances.collect())
# # Convert our RDD of strings to numeric data so we can compute stats and
# # remove the outliers.
# distanceNumerics = distances.map(lambda string: float(string))
# stats = distanceNumerics.stats()
# stddev = stats.stdev()
# mean = stats.mean()
# reasonableDistances = distanceNumerics.filter(
#     lambda x: math.fabs(x - mean) < 3 * stddev)
# print(reasonableDistances.collect())

