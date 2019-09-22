'''
'''


'''

'''
import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from termcolor import colored
import json
from pyspark.sql import SparkSession


# conf = SparkConf().setMaster('local').setAppName('PySparkShell')
# sc = SparkContext(conf=conf)


#设置log级别
# sc.setLogLevel("WARN")

input_path = 'demo.json'
# outputFile = 'demo_save'
print('-------方法1--------')
with open(input_path) as f:
    d = json.load(f)
    print(d)


print('-------方法2--------')
spark = SparkSession \
    .builder \
    .appName("PySparkShell") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext

# A JSON dataset is pointed to by path.
# The path can be either a single text file or a directory storing text files

peopleDF = spark.read.json(input_path)

# The inferred schema can be visualized using the printSchema() method
peopleDF.printSchema()
# root
# Creates a temporary view using the DataFrame
peopleDF.createOrReplaceTempView("people")

# SQL statements can be run by using the sql methods provided by spark
teenagerNamesDF = spark.sql("SELECT name FROM people WHERE age BETWEEN 13 AND 19")
teenagerNamesDF.show()


# Alternatively, a DataFrame can be created for a JSON dataset represented by
# an RDD[String] storing one JSON object per string
jsonStrings = ['{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}']
otherPeopleRDD = sc.parallelize(jsonStrings)
otherPeople = spark.read.json(otherPeopleRDD)
otherPeople.show()
