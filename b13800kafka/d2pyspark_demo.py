from pyspark import SparkContext

sc = SparkContext("local", "First App")

# 載入檔案
text_file = sc.textFile("yellow.txt")

# word count
counts = text_file.flatMap( lambda line: line.lower().split(" ") ) \
            .map( lambda word: (word, 1) ) \
            .reduceByKey( lambda a, b: a + b ) \
            .sortBy( lambda x: x[1], False )
output = counts.collect()

# 印出字與數量
for (word, count) in output:
    print( "%s: %i" % (word, count) )
    
# Stopping Spark Context
sc.stop()