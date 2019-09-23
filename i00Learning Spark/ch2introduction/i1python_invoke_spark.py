import findspark
findspark.init()

from pyspark import SparkContext
from pyspark import SQLContext
from pyspark import SparkConf


sc = SparkContext('local[*]', appName='PySparkShell')
# spark = SQLContext(sc)

#创建一个lines的RDD
lines = sc.textFile("i1introduction.md")

c = lines.count()
f = lines.first()

print('#'*20)
print(c, f)

# 筛选的例子
sparklines = lines.filter(lambda line: "Spark" in line)
p = sparklines.first()
print('p=', p)