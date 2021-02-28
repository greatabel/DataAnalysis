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
            "SELECT placeid, time, car_type_small, car_type_middle, car_type_large, car_total_num, car_speeds FROM traffic ORDER BY time desc LIMIT 10"
        )
        show1 = colored(
            "\n 1. According to lastest time order:", "blue", attrs=["reverse", "blink"]
        )
        print(
            "#" * 20,
            show1,
            topTraffics.collect(),
            " record count:",
            len(topTraffics.collect()),
        )

        for singleT in topTraffics.collect():
            print(
                singleT["time"],
                colored("'s traffic flow :", "blue"),
                singleT["car_total_num"],
            )

        # https://stackoverflow.com/questions/39535447/attributeerror-dataframe-object-has-no-attribute-map
        topTrafficText = topTraffics.rdd.map(lambda row: row.car_speeds)

        for singlelist in topTrafficText.collect():
            print("#" * 20, "\n 2. Just car_speeds", singlelist)
            isum = 0
            for speed in singlelist:
                isum += speed
            average_speed = isum / len(singlelist)
            show3 = colored(
                "3. Traffic flow sum is:", "red", attrs=["reverse", "blink"]
            )
            print(show3, isum, "Traffic flow density is:", average_speed)
        time.sleep(3)

    sc.stop()


if __name__ == "__main__":

    data_anlysis("traffic_data/traffic*.json")
