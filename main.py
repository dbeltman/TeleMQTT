import time

import schedule

from R510_SSH import get_status
from mqtt_controller import publish_telemetry


def startup():
	systemstatus = get_status()
	print(systemstatus)
	print(len(systemstatus))

	if len(systemstatus) > 0:
		ambient_temperature = float(systemstatus[2].replace('Ambient Temp      ', ''))
		fan_speed = round(float(systemstatus[3].replace('FAN MOD 1A RPM    ', '')) / 11000 * 100)
		print("Amb. Temp: " + str(ambient_temperature) + " Fan Speed: " + str(fan_speed))
		publish_telemetry(ambient_temperature, 'telemqtt/ambient-temp')
		publish_telemetry(fan_speed, 'telemqtt/fanspeed')
		return ambient_temperature + fan_speed
	else:
		print('Couldnt get status')
		return 'Couldnt get Status..'
def publish_ambient_temperature():
	systemstatus = get_status()
	ambient_temperature = float(systemstatus[2].replace('Ambient Temp      ', ''))
	publish_telemetry(ambient_temperature, 'telemqtt/ambient-temp')
	return ambient_temperature

def publish_fan_speed():
	systemstatus = get_status()
	fan_speed = round(float(systemstatus[3].replace('FAN MOD 1A RPM    ', ''))/11000*100)
	publish_telemetry(fan_speed, 'telemqtt/fanspeed')
	return fan_speed

schedule.every(1).minutes.do(publish_ambient_temperature)
schedule.every(1).minutes.do(publish_fan_speed)

startup()

while True:
	schedule.run_pending()
	time.sleep(1)
