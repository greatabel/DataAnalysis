import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from pyspark.rdd import RDD
from termcolor import colored


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")
# spark = SQLContext(sc)

nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x: x * x).collect()

for num in squared:
    print('%i ' % num )

lines = sc.parallelize(["I am abel", "hi", "Hello world"])
words = lines.flatMap(lambda line: line.split(" "))
print('words.first()=', words.first())

for i in words.take(10):
    print(colored('i==>', 'red'), i)

print('---- reduce() ----')
isum = nums.reduce(lambda x, y: x+y)
prod = nums.reduce(lambda x, y: x*y)
print('isum=', isum, 'prod=', prod)

print('--- aggregate() ----')
print('计算Rdd的平均值')
sumCount = nums.aggregate((0, 0),
               (lambda acc, value: (acc[0] + value, acc[1] + 1)),
               (lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1]))
               )
# return sumCount[0] / float(sumCount[1])

print('sumsCount=', sumCount, '#', sumCount[0] / float(sumCount[1]))