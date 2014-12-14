#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time

import config

sys.path.append("/home/pi/apps/libs")
from ds18b20 import readTemperature
from gy30 import readLuminosity
from dht22 import readHumidity
from gy65 import readPressure
from thingspeak import publishThingspeak

if __name__ == "__main__":

	thingspeak_key=config.thingspeak_wstation_key
	
	try:
		(Humi,InTemp)=readHumidity()
		print("DHT22 Humidity:\t{0} %".format(Humi))
		print("DHT22 Temp:\t{0} C".format(InTemp))

		OutTemp=readTemperature()[0] # Take value in celsius only
		print("DS18B20 Temp:\t{0} C".format(OutTemp))
		
		(Pressure, InTemp2, Altitude) = readPressure()
		print("GY65 Pressure:\t{0} hPa".format(Pressure))
		print("GY65 Temp:\t{0} C".format(InTemp2))
		print("GY65 Altitude:\t{0} m".format(Altitude))

		Luminosity = readLuminosity()
		print("GY30 Light:\t{0} lx".format(Luminosity))

		# Fields: Indoor Temp, Humidity, Outdoor Temp, Pressure, Altitude, Indoor Temp2, Luminosity, Motion
		params=(InTemp, Humi, OutTemp, Pressure, Altitude, InTemp2, Luminosity, "")
		publishThingspeak(thingspeak_key, params)

	except:
		print "Some error ocurred"

	print "Exit" 
