from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext, Row
from pyspark.sql.types import IntegerType
import json
import sys
inputFile = 'flights2008.csv'
inputFile = '/Users/abel/Downloads/spare_time/working/b13590_1.8k_spark_7月28日/flights2008.csv'

conf = SparkConf().setAppName("SparkSQLAirTransit")
SparkConf().set("spark.sql.legacy.timeParserPolicy","LEGACY")
sc = SparkContext.getOrCreate(conf=conf)
hiveCtx = HiveContext(sc)
print("Loading flights from " + inputFile)

input = hiveCtx.read.option("header",True).csv(inputFile,inferSchema =True)



input.registerTempTable("air_transit")
myair_transits = hiveCtx.sql("SELECT * FROM air_transit LIMIT 3")
print('myair_transits:' )
for item in myair_transits.collect():
	print(item, '\n')

print('1. column=',len(myair_transits.columns))
myair_transits = hiveCtx.sql("SELECT count(*) FROM air_transit ")
print('1. rows : ', myair_transits.collect())

print('2. print out the schema of this dataframe')
input.printSchema()

print('3. List the distinct carriers of in the dataframe:')
myair_transits = hiveCtx.sql("SELECT distinct UniqueCarrier FROM air_transit ")
print(myair_transits.collect())

print('4. How many flights in total are there in January:')
myair_transits = hiveCtx.sql("SELECT count(*) FROM air_transit where Month=1 ")
print(myair_transits.collect())

print('5. the total number of flights by each of the carriers')
myair_transits = hiveCtx.sql("SELECT UniqueCarrier, count(*) FROM air_transit group by UniqueCarrier ")
print('UniqueCarrier', ' count(*)')
for row in myair_transits.collect():
	print(row[0], row[1])

print('6. Count the total number of flights in the first half year (month 1-6) by each of the carriers.')
myair_transits = hiveCtx.sql("SELECT UniqueCarrier, count(*) FROM air_transit where Month <= 6 group by UniqueCarrier ")
print('UniqueCarrier', ' count(*)')
for row in myair_transits.collect():
	print(row[0], row[1])