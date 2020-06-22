import os

import paho.mqtt.publish as mqtt_publish

if os.environ.get('MQTTPORT'):
	mqttport = os.environ.get('MQTTPORT')
else:
	mqttport = 1883


def publish_telemetry(payload, topic):
	mqtt_publish.single(topic, payload,
						hostname=os.environ.get('MQTTHOST'),
						client_id=os.environ.get('MQTTCLIENT'),
						port=mqttport)
