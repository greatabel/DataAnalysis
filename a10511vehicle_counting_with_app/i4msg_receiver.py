import cv2

import time
import os

from random import choice, random


import csv
import ast


import pika
import json
import numpy
import base64
import i2rabbitmq_config


def receiver(host, processid):
    # at yangxin shuini factory
    # host = '10.248.68.249'

    # host = '127.0.0.1'
    credentials = pika.PlainCredentials("test", "test")
    parameters = pika.ConnectionParameters(host, 5672, "/", credentials)
    # detector = Hat_and_Person_Detector(processid)
    detector = "mydetector"
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(
        queue="trafficflow_spark",
        arguments=i2rabbitmq_config.ARGUMENTS,
    )

    # channel.basic_consume(on_message_callback=lambda ch, method, properties, body: image_get_v0(ch,
    #                         method, properties, body, processid=processid, detector=detector),
    #                       queue='hello',
    #                       auto_ack=True)
    channel.basic_consume(
        on_message_callback=lambda ch, method, properties, body: data_anlysis(
            ch, method, properties, body, processid=processid, detector=detector
        ),
        queue="trafficflow_spark",
        auto_ack=False,
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


def data_anlysis(ch, method, properties, body, processid, detector):
    msg = json.loads(body)
    print("data_anlysis", msg)
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    if str(msg["placeid"]) != "":
        with open(
            "traffic_data/placeid"
            + str(msg["placeid"])
            + "/traffic-"
            + str(now)
            + ".json",
            "w",
        ) as f:
            json.dump(msg, f)


if __name__ == "__main__":
    receiver(i2rabbitmq_config.Where_This_Server_ReadFrom, None)
    # now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    # print(now)