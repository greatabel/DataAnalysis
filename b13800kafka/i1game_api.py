#!/usr/bin/env python
from kafka import KafkaProducer
from flask import Flask
app = Flask(__name__)
# event_logger = KafkaProducer(bootstrap_servers='kafka:29092',api_version=(0,11,5))
event_logger = KafkaProducer(bootstrap_servers='localhost:9092',
	value_serializer=lambda x: dumps(x).encode('utf-8')
	api_version=(0,11,5))
# event_logger = KafkaProducer(bootstrap_servers='localhost:9092')
events_topic = 'events'

#curl http://127.0.0.1:5000/
@app.route("/")
def default_response():
	print('@'*10)
	event_logger.send(events_topic, 'default'.encode())
	print('in default_response')
	return "This is the default response!"

@app.route("/purchase_a_sword")
def purchase_sword():
    # business logic to purchase sword
    # log event to kafka
    event_logger.send(events_topic, 'purchased_sword'.encode())
    return "Sword Purchased!"



if __name__ == '__main__':
    app.run(debug = True)