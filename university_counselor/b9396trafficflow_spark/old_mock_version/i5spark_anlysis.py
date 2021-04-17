import findspark

findspark.init()
# A simple demo for working with SparkSQL and Traffics
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext, Row
from pyspark.sql.types import IntegerType
import json
import sys
import time
from termcolor import colored

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='handle the folder of place where save all the json of this place')
    parser.add_argument('--placeid', type=str, default='0',

                        help="Base network name which serves as feature extraction base.")
    args = parser.parse_args()
    return args


def data_anlysis(inputFile):
    # inputFile = 'tesTraffic.json'
    conf = SparkConf().setAppName("SparkSQLTraffic")
    sc = SparkContext()
    hiveCtx = HiveContext(sc)
    print("Loading traffic from " + inputFile)
    while True:
        input = hiveCtx.read.json(inputFile)
        input.registerTempTable("traffic")
        topTraffics = hiveCtx.sql(
            "SELECT placeid,size, color, direction, speed FROM traffic ORDER BY time LIMIT 10"
        )
        print("#" * 20, "\n 1. According to lastest time order:", topTraffics.collect(),' record count:', len( topTraffics.collect()))

        # https://stackoverflow.com/questions/39535447/attributeerror-dataframe-object-has-no-attribute-map
        topTrafficText = topTraffics.rdd.map(lambda row: row.speed)
        isum = 0
        for speed in topTrafficText.collect():
            print("#" * 20, "\n 2. Just speed", speed)
            
            # for speed in singlelist:
            #     print('\nspeed=', speed)
            isum += float(speed)
        average_speed = isum / len( topTraffics.collect())
        show = colored("3. total flow is:", "red", attrs=['reverse', 'blink'])
        print(show, isum, "average spped is:", average_speed)
        time.sleep(3)

    sc.stop()


if __name__ == "__main__":
    args = parse_args()
    data_anlysis("traffic_data/placeid"+ args.placeid+ "/traffic*.json")


