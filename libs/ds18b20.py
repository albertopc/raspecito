#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import glob

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

def countSensors():
	device_folder = glob.glob(base_dir + '28*')
	return len(device_folder)

def readSensorFolder(sensorId=0):
	device_folder = glob.glob(base_dir + '28*')
	return device_folder[sensorId]

def readTemperatureRaw(sensorId):
	device_folder = glob.glob(base_dir + '28*')[sensorId]
	device_file = device_folder + '/w1_slave'
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def readTemperature(sensorId=0):
    lines = readTemperatureRaw(sensorId)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readTemperatureRaw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

if __name__ == "__main__":
	print "DS18B20 Temperature sensor"
	total_sensors=countSensors()
	print "Number of sensors detected: " + format(total_sensors)
	for i in range(total_sensors):
		print ("Reading sensor [" + format(i) + 
			"," + format(readSensorFolder(i)) + "]: " +
			format(readTemperature(i)) + "(ºC, ºF)")