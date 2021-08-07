#!/usr/bin/env python
from kafka import KafkaProducer
import json
import datetime
from flask import Flask


app = Flask(__name__)

# # event_logger = KafkaProducer(bootstrap_servers='kafka:29092',api_version=(0,11,5))
# event_logger = KafkaProducer(bootstrap_servers='localhost:9092',
# 	value_serializer=lambda x: dumps(x).encode('utf-8')
# 	api_version=(0,11,5))
# # event_logger = KafkaProducer(bootstrap_servers='localhost:9092')
# events_topic = 'events'

events_topic = 'myTopic'
event_logger = KafkaProducer(bootstrap_servers='192.168.0.104:9092',
				value_serializer=lambda m:json.dumps(m).encode("utf-8"))  


#curl http://127.0.0.1:5000/
@app.route("/")
def default_response():
	# event_logger.send(events_topic, 'default'.encode())
	print('in default_response')
	data = {"ts":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
			"user_action": "default"}
	event_logger.send(events_topic, data)

	return "This is the default response!"

@app.route("/purchase_a_sword")
def purchase_sword():
    # business logic to purchase sword
    # log event to kafka
    data={"ts":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    	 "user_action": "purchased_sword"
    }
    event_logger.send(events_topic, data)
    return "Sword Purchased!"



if __name__ == '__main__':
    app.run(debug = True)