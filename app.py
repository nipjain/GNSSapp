import paho.mqtt.client as mqtt
import serial
import time

broker_address="0b45b12d2ba4443688781b3165bbcfaa.s2.eu.hivemq.cloud"
ser = serial.Serial('/dev/ttyS2',115200)
client = mqtt.Client(client_id="IR1101gps", userdata=None, protocol=mqtt.MQTTv5)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("cisco", "cisco123")
client.connect(broker_address,8883)
data = None

def publish():
    data = ser.readline()
    if not data:
       msg = client.publish("gps", 'acquiring gps coordinates')
    raw = data.rstrip().decode('utf-8')
    msg = client.publish("gps",str(data))
    return str(msg)

while 1:
    publish()
    time.sleep(2)
