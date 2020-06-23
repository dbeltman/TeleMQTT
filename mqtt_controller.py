import os

import paho.mqtt.publish as mqtt_publish

if os.environ.get('MQTTPORT'):
	mqttport = os.environ.get('MQTTPORT')
else:
	mqttport = 1883


def publish_telemetry(payload, topic):
	print("MQTT publishing to " + str(topic )+ " with payload " + str(payload) + "on host:port " + os.environ.get(
		'MQTTHOST') + str(mqttport))
	mqtt_publish.single(topic, payload,
						hostname=os.environ.get('MQTTHOST'),
						client_id=os.environ.get('MQTTCLIENT'),
						port=mqttport)
