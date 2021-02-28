import findspark
findspark.init()
# A simple demo for working with SparkSQL and Tweets
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext, Row
from pyspark.sql.types import IntegerType
import json
import sys
from termcolor import colored


inputFile = 'testweet.json'
conf = SparkConf().setAppName("SparkSQLTwitter")
sc = SparkContext()
hiveCtx = HiveContext(sc)
print("Loading tweets from " + inputFile)

input = hiveCtx.read.json(inputFile)
input.registerTempTable("tweets")
topTweets = hiveCtx.sql("SELECT text, retweetCount FROM tweets ORDER BY retweetCount LIMIT 10")
print('依据retweetCount（转发计数）选出推文=', topTweets.collect() )

# https://stackoverflow.com/questions/39535447/attributeerror-dataframe-object-has-no-attribute-map
topTweetText = topTweets.rdd.map(lambda row : row.text)
print(topTweetText.collect() )
# Make a happy person row
happyPeopleRDD = sc.parallelize([Row(name="holden", favouriteBeverage="coffee")])

#https://blog.csdn.net/m0_37870649/article/details/81603764
happyPeopleSchemaRDD = hiveCtx.createDataFrame(happyPeopleRDD)
happyPeopleSchemaRDD.registerTempTable("happy_people")
# Make a UDF to tell us how long some text is
hiveCtx.registerFunction("strLenPython", lambda x: len(x), IntegerType())
lengthSchemaRDD = hiveCtx.sql("SELECT strLenPython('text') FROM tweets LIMIT 10")
print(lengthSchemaRDD.collect() )
sc.stop()
