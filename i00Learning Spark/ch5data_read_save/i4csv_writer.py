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
outputFile = 'i4write_demo.csv'

def load_record(line):
    #解析一行csv
    inputa = StringIO(line)
    reader = csv.DictReader(inputa, fieldnames=[
        "name", "year", "addr", "d1", "d2"])
    return next(reader)

def writeRecords(records):
    """写出一些CSV记录"""
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=[
        "name", "year", "addr", "d1", "d2"])
    for record in records:
        writer.writerow(record)
    return [output.getvalue()]




inputb = sc.textFile(inputFile).map(load_record)
for i in inputb.take(10):
    print(colored('i==>', 'red'), i)

peoples = inputb.filter(lambda x: x['name'] == "Belinda Jameson")
peoples.mapPartitions(writeRecords).saveAsTextFile(outputFile)



