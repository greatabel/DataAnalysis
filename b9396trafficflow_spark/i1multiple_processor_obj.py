import cv2

import time
import multiprocessing as mp




import os

import logging
import logging.handlers
from random import choice, random


import csv
import ast

import pika
import json
import numpy
import base64
import i13rabbitmq_config
#https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks


rtsp_file_path = 'i0rtsp_list.csv'
queue_rtsp_dict = {}
img_name = ''

# MXNet报Running performance tests to find the best convolution algorithm
os.environ["MXNET_CUDNN_AUTOTUNE_DEFAULT"] = "0"

def listener_configurer():
    # logging.getLogger("pika").propagate = False

    root = logging.getLogger()
    h = logging.handlers.RotatingFileHandler('temp.log', 'a', 3000000, 10)
    f = logging.Formatter('%(asctime)s %(processName)-8s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)

# This is the listener process top-level loop: wait for logging events
# (LogRecords)on the queue and handle them, quit when you get a None for a
# LogRecord.
def listener_process(queue, configurer):
    configurer()
    while True:
        try:
            record = queue.get()

            if record is None:  # We send this as a sentinel to tell the listener to quit.
                break
            if 'pika' in record.name:
                print('-'*30, record, '-'*30)
            elif 'pika' not in record.name:
                                # print('record','*'*20,record.name, record)
                logger = logging.getLogger(record.name)
                # logger.handle(record)  # No level or filter logic applied - just do it!
                warning_processor(logger, record)
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)


queueid_warning_dict = {}
queueid_lastsendtime_dict = {}


class Hat_and_Person_Detector():
    def __init__(self, processid, log_queue):
        print('processid', processid, '-^-'*5)
        self.log_queue = log_queue

      



    def process(self, frame,  rect, default_enter_rule, queueid=None):
        h = logging.handlers.QueueHandler(self.log_queue)  # Just the one handler needed
        root = logging.getLogger()
        root.addHandler(h)
        # send all messages, for demo; no other level or filter logic applied.
        root.setLevel(logging.DEBUG)

        logger = logging.getLogger(str(queueid))
        if frame is not None:
            print('here0', rect, default_enter_rule, type(frame))

            cv2.namedWindow("image", cv2.WINDOW_NORMAL)
            cv2.imshow('image', frame)
            
            print('processing:', queueid)

            # if cv2.waitKey(1) == 27:
            #         break
        else:
            print('skip frame from queueid=', queueid)


def receiver(host, processid, log_queue):

    # host = '127.0.0.1'
    credentials = pika.PlainCredentials('test', 'test')
    parameters = pika.ConnectionParameters(host,
                                       5672,
                                       '/',
                                       credentials)
    detector = Hat_and_Person_Detector(processid, log_queue)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(
        queue='hello',
        arguments=i13rabbitmq_config.ARGUMENTS,
        )

    # channel.basic_consume(on_message_callback=lambda ch, method, properties, body: image_get_v0(ch, 
    #                         method, properties, body, processid=processid, detector=detector),
    #                       queue='hello',
    #                       auto_ack=True)
    channel.basic_consume(on_message_callback=lambda ch, method, properties, body: image_get_v0(ch, 
                            method, properties, body, processid=processid, detector=detector),
                          queue='hello',
                           auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()






# def image_get_v0(quelist, window_name, log_queue):
def image_get_v0(ch, method, properties, body, processid, detector):



    # cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    print('************************************')


    print('in image_get_v0 ', ch, method, properties, 'processid==>', processid)
    msg = json.loads(body)
    frame = None
    if msg is not None:
        img = base64.b64decode(msg['img'].encode())
        
        # get image array
        frame = cv2.imdecode(numpy.fromstring(img, numpy.uint8), 1)

        # frame = numpy.asarray(msg["img"])
        queueid = int(msg['placeid'])
        # print(" [x] Received %r" % msg)
        # imgdata = base64.b64decode(msg['img'])
        print(msg['placeid'], '@'*10, msg['time'])
        print(type(frame), '#'*10)
        cv2.imwrite("filename.png", frame)

        print('-----------------------')

        # print(queue_rtsp_dict, queueid, type(queueid))
        # frame, queueid = q.get()
        rect = None 
        print(queue_rtsp_dict, queueid, '$'*20)
        if queue_rtsp_dict.get(queueid, None)[7] != None and \
             queue_rtsp_dict.get(queueid, None)[7].strip() != '':
            print('#'*30, 'here')
            rect = ast.literal_eval(queue_rtsp_dict.get(queueid, None)[7])
        default_enter_rule = queue_rtsp_dict.get(queueid, None)[8]
        detector.process(frame, rect, default_enter_rule, queueid)




def run_multi_camera(camera_ip_l):
    global queue_rtsp_dict
    for line in camera_ip_l:
        print('line:', line, type(line))
        queue_rtsp_dict[int(line[0])] = line[1:]
    log_queue = mp.Queue(-1)
    listener = mp.Process(target=listener_process,
                                       args=(log_queue, listener_configurer))
    listener.start()

    # mp.set_start_method(method='spawn')  # init0
    queues = [mp.Queue(maxsize=4) for _ in camera_ip_l]
    processes = []



    # -------------------- start ai processes
    num_of_ai_process = 2

    for i in range(0, num_of_ai_process):
        print('ai process', i)
        processes.append(mp.Process(target=receiver, args=(i13rabbitmq_config.Where_This_Server_ReadFrom,
                                                           i, log_queue)))
    # -------------------- end   ai processes

    for process in processes:
        process.daemon = True
        process.start()
    for process in processes:
        process.join()


def load_rtsp_list():
    with open(rtsp_file_path, newline='') as f:
        reader = csv.reader(f)
        rtsp_list = list(reader)
    # print(data, '#'*10, data[0],'\n', data[0][0])
    return rtsp_list

if __name__ == '__main__':
    camera_ip_l = load_rtsp_list()
    # python3 i13multiple_processor_obj.py --gpu=True --network=yolo3_mobilenet0.25_voc
    run_multi_camera(camera_ip_l) 
