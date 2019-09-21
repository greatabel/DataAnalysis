'''
DISK_ONLY = StorageLevel(True, False, False, False, 1)

DISK_ONLY_2 = StorageLevel(True, False, False, False, 2)

MEMORY_AND_DISK = StorageLevel(True, True, False, False, 1)

MEMORY_AND_DISK_2 = StorageLevel(True, True, False, False, 2)

MEMORY_AND_DISK_SER = StorageLevel(True, True, False, False, 1)

MEMORY_AND_DISK_SER_2 = StorageLevel(True, True, False, False, 2)

MEMORY_ONLY = StorageLevel(False, True, False, False, 1)

MEMORY_ONLY_2 = StorageLevel(False, True, False, False, 2)

MEMORY_ONLY_SER = StorageLevel(False, True, False, False, 1)

MEMORY_ONLY_SER_2 = StorageLevel(False, True, False, False, 2)

OFF_HEAP = StorageLevel(True, True, True, False, 1)

Let us consider the following example of StorageLevel, 
where we use the storage level MEMORY_AND_DISK_2, 
which means RDD partitions will have replication of 2

--------------------
https://www.tutorialspoint.com/pyspark/pyspark_storagelevel.htm

'''

import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
from pyspark import SparkConf
from pyspark import StorageLevel
from termcolor import colored


conf = SparkConf().setMaster('local').setAppName('PySparkShell')
sc = SparkContext(conf=conf)

#设置log级别
sc.setLogLevel("WARN")
# spark = SQLContext(sc)

#创建一个lines的RDD
lines = sc.parallelize(['pandas demo', 'I like pandas', 'hello world'])

# 遍历结果
pandaslines = lines.filter(lambda line: "pandas" in line)
print(colored('把RDD持久化到内存中', 'red'))
pandaslines.persist( StorageLevel.MEMORY_AND_DISK_2 )

print('getStorageLevel=', pandaslines.getStorageLevel())

for i in pandaslines.collect():
    print(colored('i==>', 'red'), i)