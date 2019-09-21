# import findspark
# findspark.init()

from pyspark import SparkContext
from pyspark import SQLContext
from pyspark import SparkConf

# import os

# os.environ['PYSPARK_SUBMIT_ARGS'] = "--master local[2] pyspark-shell"
# os.environ['JAVA_HOME']  = "$(/usr/libexec/java_home -v 13)"

#################### spark调用python文件： ####################
# spark-submit i0spark-submit-demo.py



sc = SparkContext("local","PySparkShell")
spark = SQLContext(sc)


lines = sc.textFile("README.md")

c = lines.count()
f = lines.first()

print('#'*20)
print(c, f)