import findspark

findspark.init()
# A simple demo for working with SparkSQL and vehicless
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext, Row
from pyspark.sql.types import IntegerType
import json
import sys
import time
from termcolor import colored

import random
import argparse
from datetime import date
import calendar
import os
import datetime



def count_files_in_folder(path):

    dirListing = os.listdir(path)

    file_count = len(dirListing)
    return file_count

def data_anlysis():

    inputFile =  "data/vehicles.csv"
    

    # inputFile = 'tesvehicles.json'
    conf = SparkConf().setAppName("SparkSQLvehicles")
    sc = SparkContext()
    hiveCtx = HiveContext(sc)
    print("Loading vehicles from " + inputFile)
    while True:
        # prev_count = count_files_in_folder(inputPath)
        input = hiveCtx.read.json(inputFile)
        input.registerTempTable("vehicles")
        topvehicless = hiveCtx.sql(
            "SELECT region, price,year, price,year, FROM vehicles ORDER BY id LIMIT 20"
        )
        print(
            "#" * 20,
            "\n 1. According to lastest id order:",
            topvehicless.collect(),
            " record count:",
            len(topvehicless.collect()),
        )

        print(colored("2. filter out now span data:", "blue", attrs=["reverse", "blink"]))


    sc.stop()


if __name__ == "__main__":
    data_anlysis()
    # python3 i5spark_anlysis.py
