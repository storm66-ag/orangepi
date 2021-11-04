#!/usr/bin/python3
from flask import Flask, render_template
from pyA20.gpio import gpio
from pyA20.gpio import port

import dht
import time

import os
import sys
module_path = os.path.abspath(os.getcwd() + '\\..')
if module_path not in sys.path:
    sys.path.append(module_path)


app = Flask(__name__)

gpio.init()
DHT22_PIN = port.PA6
DHT22_instance = dht.DHT22(pin=DHT22_PIN)
DHT22_result = DHT22_instance.read()
###

@app.route('/')
def index():
    return "This is the index page"

@app.route('/humidity', methods=['GET'])
def get_humidity():
    humidity = DHT22_result.humidity/22
    return str(humidity)

@app.route('/temperature', methods=['GET'])
def get_temperature():
    temperature = DHT22_result.temperature/22
    return str(temperature)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)
