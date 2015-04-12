#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys, getopt
import time
import datetime

import config

sys.path.append("/home/pi/apps/libs")
from ds18b20 import readTemperature
from gy30 import readLuminosity
from dht22 import readHumidity
from gy65 import readPressure
from thingspeak import publishThingspeak
from display import display_text



if __name__ == "__main__":
	publish=1
	display=1
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hdp",["help","display-only","publish-only"])
	except getopt.GetoptError:
		print 'wstation.py [-d]'
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h","help"):
			print 'wstation.py -d'
			sys.exit()
		elif opt in ("-d", "--display-only"):
			publish=0
		elif opt in ("-p", "--publish-only"):
			display=0

	thingspeak_key=config.thingspeak_wstation_key
	
	try:
		ahora=datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
		print(ahora)
		if display==1:
			display_text(0,0, ahora)
		
		(Humi,InTemp)=readHumidity()
		print("DHT22 Humidity:\t{0} %".format(Humi))
		print("DHT22 Temp:\t{0} C".format(InTemp))

		OutTemp=readTemperature()[0] # Take value in celsius only
		print("DS18B20 Temp:\t{0} C".format(OutTemp))

		if display==1:
			display_text(0,12, "{:.2f} C".format(OutTemp))
			display_text(65,12, "{0} %".format(Humi))
		
		(Pressure, InTemp2, Altitude) = readPressure()
		print("GY65 Pressure:\t{0} hPa".format(Pressure))
		print("GY65 Temp:\t{0} C".format(InTemp2))
		print("GY65 Altitude:\t{0} m".format(Altitude))
		if display==1:
			display_text(0,22, "{0} hPa".format(Pressure))	
		
		Luminosity = readLuminosity()
		print("GY30 Light:\t{0} lx".format(Luminosity))
		if display==1:
			display_text(65,22, "{:.2f} lx".format(Luminosity))	

		if publish == 1:
			# Fields: Indoor Temp, Humidity, Outdoor Temp, Pressure, Altitude, Indoor Temp2, Luminosity, Motion
			params=(InTemp, Humi, OutTemp, Pressure, Altitude, InTemp2, Luminosity, "")
			publishThingspeak(thingspeak_key, params)

	except:
		print "Some error ocurred"

	print "Exit" 
