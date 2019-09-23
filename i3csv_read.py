import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from termcolor import colored
import csv
from io import StringIO


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")

inputFile = 'i3demo.csv'

def load_record(line):
    #解析一行csv
    inputa = StringIO(line)
    reader = csv.DictReader(inputa, fieldnames=[
        "name", "year", "addr", "d1", "d2"])
    return next(reader)

inputb = sc.textFile(inputFile).map(load_record)
for i in inputb.take(10):
    print(colored('i==>', 'red'), i)



print('\n-- 在 Python 中完整读取 CSV --\n')
def load_all_records(filenamecontents):
    inputa = StringIO(filenamecontents[1])
    reader = csv.DictReader(inputa, fieldnames=[
        "name", "year", "addr", "d1", "d2"])
    return reader

inputc = sc.wholeTextFiles(inputFile).flatMap(load_all_records)
for i in inputc.take(10):
    print(colored('i==>', 'green'), i)