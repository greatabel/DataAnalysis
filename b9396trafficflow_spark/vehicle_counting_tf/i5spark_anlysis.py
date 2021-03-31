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
    parser = argparse.ArgumentParser(
        description="handle the folder of place where save all the json of this place"
    )
    parser.add_argument(
        "--placeid",
        type=str,
        default="0",
        help="Base network name which serves as feature extraction base.",
    )
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
            "SELECT placeid,size, color, direction, speed FROM traffic ORDER BY time desc LIMIT 10"
        )
        print(
            "#" * 20,
            "\n 1. According to lastest time order:",
            topTraffics.collect(),
            " record count:",
            len(topTraffics.collect()),
        )

        # https://stackoverflow.com/questions/39535447/attributeerror-dataframe-object-has-no-attribute-map
        topTrafficText = topTraffics.rdd.map(lambda row: (row.speed, row.direction))
        down_sum, up_sum = 0, 0
        for (speed, direction) in topTrafficText.collect():
            print("#" * 20, "\n 2. Just speed", speed, ' direction=', direction)

            # for speed in singlelist:
            #     print('\nspeed=', speed)
            if speed != 'n.a.':
                if direction == 'down':
                    down_sum += float(speed)
                elif direction == 'up':
                    up_sum += float(speed)
        average_speed = (down_sum + up_sum) / len(topTraffics.collect())
        show = colored("3. total flow is:", "red", attrs=["reverse", "blink"])
        print(show, 'total down flow=', down_sum, 'total up flow=', up_sum, "average spped is:", average_speed)
        time.sleep(3)

    sc.stop()


if __name__ == "__main__":
    args = parse_args()
    data_anlysis("traffic_data/placeid" + args.placeid + "/traffic*.json")
    # python3 i5spark_anlysis.py --placeid=0
