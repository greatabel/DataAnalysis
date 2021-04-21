import pika
import json
from json import JSONEncoder
import numpy as np
import time
import cv2
import base64

import i2rabbitmq_config


# class NumpyArrayEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, numpy.ndarray):
#             return obj.tolist()
#         return JSONEncoder.default(self, obj)


def sender(
    host, size, color, direction, speed, queueid=None, queue_name="trafficflow_spark"
):
    print(queueid, "in sender", queue_name)

    credentials = pika.PlainCredentials("test", "test")
    parameters = pika.ConnectionParameters(host, 5672, "/", credentials)

    connection = pika.BlockingConnection(parameters)
    # connection = pika.BlockingConnection(pika.ConnectionParameters(
    #         host=host))
    channel = connection.channel()

    channel.queue_declare(
        queue=queue_name,
        arguments=i2rabbitmq_config.ARGUMENTS,
    )

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    #  保留威将来，如果需要把模拟的图片数据处理，变成真实的

    # _, img_encode = cv2.imencode('.jpg', img)
    # np_data = np.array(img_encode)
    # str_data = np_data.tostring()
    # b64_bytes = base64.b64encode(str_data)

    # picData_string = b64_bytes.decode()

    msg = {
        "placeid": queueid,
        "time": now,
        # 'img': picData_string
        "size": size,
        "color": color,
        "direction": direction,
        "speed": speed,
    }
    print("placeid=", queueid, msg)
    # print(type(msg), '@'*10, 'msg=', msg)
    json0 = json.dumps(msg)
    # import codecs
    # with codecs.open('data.json', 'w', 'utf8') as outfile:
    #     outfile.write(json.dumps(msg,cls=NumpyArrayEncoder))
    import sys

    s = sys.getsizeof(msg)
    s0 = sys.getsizeof(json0)
    print(s0, s0 / 1024, s0 / 1048576, type(json0))
    channel.basic_publish(exchange="", routing_key=queue_name, body=json0)
    print("rabbitMQ [x] Sent msg'", "-" * 20)
    connection.close()


if __name__ == "__main__":
    numpyArrayOne = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
    sender("localhost", 100, None, None, None)
