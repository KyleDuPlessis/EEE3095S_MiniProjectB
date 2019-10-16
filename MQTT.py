# Import package
import paho.mqtt.client as mqtt
import time

time.sleep(5) #Sleep to allow wireless to connect before starting MQTT

# Define Variables
MQTT_BROKER = "192.168.137.15"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
    print("Connected to MQTT Broker")

# Define on_publish event Handler
def on_publish(client, userdata, mid):
    print("Message Published...")

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register Event Handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

# Connect with MQTT Broker
mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)


mqttc.loop_start()

topic_RTCTime = "pi/RTCTime"
topic_SystemTimer = "pi/SystemTimer"
topic_HumidityReading = "pi/HumidityReading"
topic_TemperatureReading = "pi/TemperatureReading"
topic_LightReading = "pi/LightReading"
topic_DACOut = "pi/DACOut"
topic_Alarm = "pi/Alarm"

# while True:

RTCTime = str(temp11)
mqttc.publish(topic_RTCTime, payload=RTCTime, retain=True)

SystemTimer = str(temp11)
mqttc.publish(topic_SystemTimer, payload=SystemTimer, retain=True)

HumidityReading = str(temp11)
mqttc.publish(topic_HumidityReading, payload=HumidityReading, retain=True)

TemperatureReading = str(temp11)
mqttc.publish(topic_TemperatureReading, payload=TemperatureReading, retain=True)

LightReading = str(temp11)
mqttc.publish(topic_LightReading, payload=LightReading, retain=True)

DACOut = str(temp11)
mqttc.publish(topic_DACOut, payload=DACOut, retain=True)

Alarm = str(temp11)
mqttc.publish(topic_Alarm, payload=Alarm, retain=True)















# Publish message to MQTT Topic
mqttc.publish(MQTT_TOPIC, MQTT_MSG)

# Disconnect from MQTT_Broker
mqttc.disconnect()
