import findspark
findspark.init()

from pyspark import SparkContext
from pyspark import SQLContext
from pyspark import SparkConf


sc = SparkContext('local[*]')
# spark = SQLContext(sc)


lines = sc.textFile("README.md")

c = lines.count()
f = lines.first()

print('#'*20)
print(c, f)