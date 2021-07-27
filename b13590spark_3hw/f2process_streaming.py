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

k_v = {}

def result(y):
	global k_v
	taken = y.take(6)

	for record in taken[:6]:
	    print(record,'#')
	    if record[0] not in k_v:
	    	k_v[record[0] ] = record[1]

	print('k_v=', k_v)

		
	if 'a' in k_v and 'b' in k_v and 'c' in k_v:
		v_a = 8*8*8 * k_v['a'] / (k_v['a'] + k_v['a_out'] )
		v_b = 4*4*4  * k_v['b'] / (k_v['b'] + k_v['b_out'] )
		v_c = 8*8*8 * k_v['c'] / (k_v['a'] + k_v['c_out'] )
		v_d = v_a + v_b  - v_c
		print('v_a = ', v_a)
		print('v_b = ', v_b)
		print('v_c = ', v_c)
		print('v_d = ', v_d)
		return y

rdd = wordCounts.foreachRDD(result)


ssc.start()
ssc.awaitTermination()
