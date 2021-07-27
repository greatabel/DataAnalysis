import sys
import random
from operator import add

from pyspark.sql import SparkSession


def a(_):
    x = random.uniform(-4, 4)
    y = random.uniform(2-4, 2+4)
    z = random.uniform(1-4, 1+4)
    return 1 if x ** 2 + (y - 2) ** 2 + (z - 1) ** 2 <= 16 else 0

def b(_):
    x = random.uniform(0, 2)
    y = random.uniform(0, 2)

    return 1 if x ** 2 + y ** 2  <= 4  else 0

def c(_):
    x = random.uniform(-4, 4)
    y = random.uniform(2-4, 2+4)
    z = random.uniform(1-4, 1+4)
    if x ** 2 + (y - 2) ** 2 + (z - 1) ** 2 <= 16 and x ** 2 + y ** 2  <= 4 and \
        z >= 0 and z <= 4 :
        return 1  
    else:
        return 0



if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession\
        .builder\
        .appName("PythonPi")\
        .getOrCreate()

    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * partitions
    print('n=', n)


    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(a).reduce(add)
    v_a = 8*8*8 * count / n
    print("volume of OA is roughly %f" % (v_a))

    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(b).reduce(add)
    v_b = 4*4*4 * count / n
    print("volume of OB is roughly %f" % (v_b))

    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(c).reduce(add)
    v_c = 8*8*8 * count / n
    print("volume of OC is roughly %f" % (v_c))

    # count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(a).reduce(add)
    v_d = v_a + v_b  - v_c
    print("volume of OD is roughly %f" % (v_d))

    spark.stop()