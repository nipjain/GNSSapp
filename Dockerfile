FROM arm64v8/python:3.8-slim
ADD app.py /
WORKDIR /
EXPOSE 8883
RUN pip install pyserial paho-mqtt minimalmodbus
ENTRYPOINT python app.py
