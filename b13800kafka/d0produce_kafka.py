# start
# kafka osx: http://www.seaxiang.com/blog/QVVJ32
# localip: 192.168.0.104
'''
start kafka:

docker run -d --name kafka \
-p 9092:9092 \
-e KAFKA_BROKER_ID=0 \
-e KAFKA_ZOOKEEPER_CONNECT=192.168.0.104:2181 \
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.0.104:9092 \
-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 wurstmeister/kafka


### create topic ##

bin/kafka-topics.sh --create --zookeeper 192.168.0.104:2181 --replication-factor 1 --partitions 1 --topic mykafka

### producer ##

bin/kafka-console-producer.sh --broker-list localhost:9092 --topic mykafka


### consumer ##

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mykafka --from-beginning

'''

# event_logger = KafkaProducer(bootstrap_servers='localhost:9092')
# -*- coding: UTF-8 -*-
from kafka import KafkaProducer
import json
import datetime

topic='myTopic'
producer = KafkaProducer(bootstrap_servers='192.168.0.104:9092',value_serializer=lambda m:json.dumps(m).encode("utf-8"))  
# 连接kafka
# 参数bootstrap_servers：指定kafka连接地址
# 参数value_serializer：指定序列化的方式，我们定义json来序列化数据，当字典传入kafka时自动转换成bytes
# 用户密码登入参数
# security_protocol="SASL_PLAINTEXT"
# sasl_mechanism="PLAIN"
# sasl_plain_username="maple"
# sasl_plain_password="maple"

for i in range(1000):
    data={"num":i,"ts":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    producer.send(topic,data)

producer.close()