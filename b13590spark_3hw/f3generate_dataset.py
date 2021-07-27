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
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    z = random.uniform(-1, 1)
    if x ** 2 + y ** 2 + z ** 2 <= 1:
        return x,y,z,0
    else:
        return 0

def b():
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    z = random.uniform(2, 4)
    if x ** 2 + y ** 2  <= 4 and (z >= 2 and z <= 4):
        return x,y,z,1
    else:
        return 0


def c():
    x = random.uniform(1, 3)
    y = random.uniform(-1, 1)
    z = random.uniform(-1, 1)
    if (x-2)**2 /1.3 + y**2/1.4 + z ** 2/4 <= 1:
        return x,y,z,2
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
        # print(now, ' # '*8)

        


        mylist = []
        for i in range(1, n + 1):
            aa = a()
            bb = b()
            cc = c()
            if aa != 0:
                mylist.append(aa)
            elif bb != 0:
                mylist.append(bb)
            elif cc != 0:
                mylist.append(cc)
        for line in mylist:
            print(str(line[0])+','+str(line[1])+','+str(line[2])+','+str(line[3]))

if __name__ == "__main__":
    data_anlysis()

# To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
# n= 200000
# volume of OA is roughly 268.139520                                              
# volume of OB is roughly 50.153920
# volume of OC is roughly 47.073280
# volume of OD is roughly 271.220160
