# -*- coding: UTF-8 -*-
from kafka import KafkaConsumer
import time
import ast

topic = 'myTopic'
consumer = KafkaConsumer(topic, bootstrap_servers=['192.168.0.104:9092'], group_id="test", auto_offset_reset="earliest")

'''
https://medium.com/@bee811101/%E4%BD%BF%E7%94%A8-docker-%E5%BF%AB%E9%80%9F%E5%BB%BA%E7%BD%AE-pyspark-%E7%92%B0%E5%A2%83-657f9d8bff3a

docker run -it --rm -p 8888:8888 -v /Users/greatabel:/home/jovyan/work jupyter/pyspark-notebook

Apache Bench
https://xushanxiang.com/2019/10/mac-web-ab.html
'''
def current_milli_time():
    return round(time.time() * 1000)


for msg in consumer:
	recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
	print(recv)
	dict_str = msg.value.decode("UTF-8")
	mydata = ast.literal_eval(dict_str)
	print('mydata=', mydata)
	with open("logfile/"+ str(current_milli_time()) +"Output.txt", "w") as text_file:
		text_file.write(mydata['user_action'])


print('##finished')