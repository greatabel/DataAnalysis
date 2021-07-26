from operator import add
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
conf = SparkConf()
conf.setAppName('TestDStream')
conf.setMaster('local[2]')
sc = SparkContext(conf = conf)
ssc = StreamingContext(sc, 20)
lines = ssc.textFileStream('file:///Users/abel/Downloads/AbelProject/DataAnalysis/b13590spark_3hw/logfile')

words = lines.flatMap(lambda line: line.split(' '))
print('-'*10, words)
wordCounts = words.map(lambda x : (x,1)).reduceByKey(add)
wordCounts.pprint()
ssc.start()
ssc.awaitTermination()
