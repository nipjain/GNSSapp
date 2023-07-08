# GNSSapp

Simple Python app to stream data from GNSS module on the IR1800 and send to MQTT topic 

1. docker build -t gps .
2. ./ioxclient docker package gps .
3. use the OD or local manager to upload the start the APP
4. user gnss_dr as the serial interface for IOX to stream data

SAMPLE Output will give gyro/accel data as well - you will need to parse the GPS data out. but this is the idea:


eg output:

b'$GPRMC,050600.000,A,3726.5177,N,12155.0149,W,0.00,0.00,080723,,,A*7B\r\n'
b'DGYRO,43053230,-45,4,-89,0,209*51\r\n'
b'STM3DGYRO,45031074,-41,-12,-83,0,211*4C\r\n'
b'SENMSG,30,46324694,-165,173,16341*35\r\n'
b'4,200,16345*3B\r\n'
b'SG,30,50553209,-176,218,16368*33\r\n'
