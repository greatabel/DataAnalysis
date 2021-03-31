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

import random
import argparse
from datetime import date
import calendar


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


def data_anlysis(placeid):
    inputFile = "traffic_data/placeid" + placeid + "/traffic*.json"
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
            print("#" * 20, "\n 2. Just speed", speed, " direction=", direction)

            # for speed in singlelist:
            #     print('\nspeed=', speed)
            if speed != "n.a.":
                if direction == "down":
                    down_sum += float(speed)
                elif direction == "up":
                    up_sum += float(speed)
        average_speed = (down_sum + up_sum) / len(topTraffics.collect())
        show = colored("3. total flow is:", "red", attrs=["reverse", "blink"])
        print(
            show,
            "total down flow=",
            down_sum,
            "total up flow=",
            up_sum,
            "average spped is:",
            average_speed,
        )

        print(colored("@" * 30, "green"), "\n--- async summary record to history ---")
        my_date = date.today()
        t0 = calendar.day_name[my_date.weekday()]
        t1 = time.strftime("%H:%M")

        # 添加random，防止因为时间短，训练数据雷同
        down_sum = down_sum * random.uniform(0, 0.8)
        up_sum = up_sum * random.uniform(1, 1.5)

        record0 = t0 + ',' + t1 + ',' + "placeid"+placeid + ",down," + str(round(down_sum, 2)) + "\n"
        record1 = t0 + ',' + t1 + ',' + "placeid"+placeid + ",up," + str(round(up_sum, 2)) + "\n"

        print(record0)
        print(record1)

        with open("i8predict_flow/history_traffic_measurement.txt", "a") as myfile:
            myfile.write(record0)
            myfile.write(record1)
        time.sleep(5)

    sc.stop()


if __name__ == "__main__":
    args = parse_args()
    data_anlysis(args.placeid)
    # python3 i5spark_anlysis.py --placeid=0
