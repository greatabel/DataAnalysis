import cv2

import time
import os

from random import randint


import csv
import ast


import pika
import json
import numpy
import base64

import datetime


def current_milli_time():
    return round(time.time() * 1000)

def data_anlysis():
    while True:
        time.sleep(5)
        now = datetime.datetime.now()
        print(now, ' # '*8)
        with open("logfile/"+ str(current_milli_time()) +"Output.txt", "w") as text_file:
            num1= randint(0,9)
            text_file.write("test %d" % num1)

if __name__ == "__main__":
    data_anlysis()