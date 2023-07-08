# GNSSapp

Simple Python app to stream data from GNSS module on the IR1800 and send to MQTT topic 

1. docker build -t gps .
2. ./ioxclient docker package gps .
3. use the OD or local manager to upload the start the APP
4. user gnss_dr as the serial interface for IOX to stream data
