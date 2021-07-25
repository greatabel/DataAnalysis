import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from pyspark.sql.functions import col
from pyspark.sql import HiveContext
from termcolor import colored
import numpy as np 


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#stop
# sc.stop()

#设置log级别
sc.setLogLevel("WARN")
spark = SQLContext(sc)

q2a = colored('---------Q2 a ---------', 'red', attrs=['reverse', 'blink'])
print(q2a)


x = [1, 2, 3, 4]
y = [20, 30, 40, 50]
print('1. definition of X, and Y:', x, y)

print('2. map x, y with zip() on dataframe:')
df = spark.createDataFrame(zip(x, y), schema=['a', 'b'])
print(df.collect())


df1 = df.select(((col("a") + col("b"))).alias("mymin"))
df1.show()
print('3. reduce by run agg func on sum columns of dataframe:')
row1 = df1.agg({"mymin": "min"}).collect()[0]
print(row1,type(row1),row1[0])

q2b = colored('---------Q2 b ---------', 'green', attrs=['reverse', 'blink'])
print(q2b)

x1 = [1, 2, 3, 4]
A = np.array([
	[1,20],
	[3,40],
	[5,60],
	[7,80]
	])
print('start with x, A:', x, A)
y1 = []

for c in range(A.shape[1]):
	a_i =  A[:,c].tolist()
	# print(type(a_i), '#'*10, a_i, 'x=',type(x1), x1)
	df_b0 = spark.createDataFrame(zip(x1, a_i), schema=["a", "b"])
	df1 = df_b0.select(((col("a") + col("b"))).alias("mymin"))
	print('map:', df1.collect())
	row1 = df1.agg({"mymin": "min"}).collect()[0][0]
	print('reduce working:', row1)
	y1.append(row1)
	# rowb1 = df_b1.agg({"mymin2": "min"}).collect()[0][0]
	# print(rowb1)
print("Y=", y1)