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
import os
import datetime


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

def count_files_in_folder(path):

    dirListing = os.listdir(path)

    file_count = len(dirListing)
    return file_count

def data_anlysis(placeid):
    inputPath = "traffic_data/placeid" + placeid
    inputFile =  inputPath + "/traffic*.json"
    

    # inputFile = 'tesTraffic.json'
    conf = SparkConf().setAppName("SparkSQLTraffic")
    sc = SparkContext()
    hiveCtx = HiveContext(sc)
    print("Loading traffic from " + inputFile)
    while True:
        prev_count = count_files_in_folder(inputPath)
        input = hiveCtx.read.json(inputFile)
        input.registerTempTable("traffic")
        topTraffics = hiveCtx.sql(
            "SELECT placeid,size, color, direction, speed, time FROM traffic ORDER BY time desc LIMIT 20"
        )
        print(
            "#" * 20,
            "\n 1. According to lastest time order:",
            topTraffics.collect(),
            " record count:",
            len(topTraffics.collect()),
        )

        print(colored("2. filter out now span data:", "blue", attrs=["reverse", "blink"]))
        # https://stackoverflow.com/questions/39535447/attributeerror-dataframe-object-has-no-attribute-map
        topTrafficText = topTraffics.rdd.map(lambda row: (row.speed, row.direction, row.time))
        down_sum, up_sum = 0, 0
        for (speed, direction, row_time) in topTrafficText.collect():
            # print('time=', row_time, type(row_time))
            record_dt = datetime.datetime.strptime(row_time,'%Y-%m-%d %H:%M:%S')
            dnow = datetime.datetime.now()
            if abs(dnow- record_dt) < datetime.timedelta(minutes=1):
                print('time =', dnow, record_dt)
                print("#" * 20, "\n 2.1 Just speed", speed, " direction=", direction)

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

        # 发生了变化，说明至少至少有数据符合时间间隔
        if down_sum!=0 or up_sum!= 0 :
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

        now_count = count_files_in_folder(inputPath)
        while now_count == prev_count:
            time.sleep(5)
            prev_count = now_count
            now_count = count_files_in_folder(inputPath)
            print('in waiting...', prev_count, now_count)

    sc.stop()


if __name__ == "__main__":
    args = parse_args()
    data_anlysis(args.placeid)
    # python3 i5spark_anlysis.py --placeid=0