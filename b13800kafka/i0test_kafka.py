from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
	value_serializer=lambda x: dumps(x).encode('utf-8'),
	api_version=(0,11,5))

# http://www.seaxiang.com/blog/QVVJ32
# localip: 192.168.0.104
'''
start kafka:

docker run -d --name kafka \
-p 9092:9092 \
-e KAFKA_BROKER_ID=0 \
-e KAFKA_ZOOKEEPER_CONNECT=192.168.0.104:2181 \
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.0.104:9092 \
-e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 wurstmeister/kafka

'''

# event_logger = KafkaProducer(bootstrap_servers='localhost:9092')
events_topic = 'events'


for j in range(10):
    print("Iteration", j)
    data = {'counter': j}
    producer.send(events_topic, 'default'.encode())
    sleep(0.5)