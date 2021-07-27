import time
import os
from random import randint

import json
import numpy
import datetime

import sys
import random
from operator import add



def a():
    x = random.uniform(-4, 4)
    y = random.uniform(2-4, 2+4)
    z = random.uniform(1-4, 1+4)
    return 1 if x ** 2 + (y - 2) ** 2 + (z - 1) ** 2 <= 16 else 0

def b():
    x = random.uniform(0, 2)
    y = random.uniform(0, 2)

    return 1 if x ** 2 + y ** 2  <= 4  else 0

def c():
    x = random.uniform(-4, 4)
    y = random.uniform(2-4, 2+4)
    z = random.uniform(1-4, 1+4)
    if x ** 2 + (y - 2) ** 2 + (z - 1) ** 2 <= 16 and x ** 2 + y ** 2  <= 4 and \
        z >= 0 and z <= 4 :
        return 1  
    else:
        return 0


def current_milli_time():
    return round(time.time() * 1000)

def data_anlysis():
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100 * partitions
    print('n=', n)

    while True:
        time.sleep(5)
        now = datetime.datetime.now()
        print(now, ' # '*8)

        

        with open("logfile/"+ str(current_milli_time()) +"Output.txt", "w") as text_file:
            mylist = []
            for i in range(1, n + 1):
                if a() == 1:
                    mylist.append('a')
                else:
                    mylist.append('a_out')
                if b() == 1:
                    mylist.append('b')
                else:
                    mylist.append('b_out')
                if c() == 1:
                    mylist.append('c')
                else:
                    mylist.append('c_out')
            text_file.write(' '.join(mylist))

if __name__ == "__main__":
    data_anlysis()

# To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
# n= 200000
# volume of OA is roughly 268.139520                                              
# volume of OB is roughly 50.153920
# volume of OC is roughly 47.073280
# volume of OD is roughly 271.220160
