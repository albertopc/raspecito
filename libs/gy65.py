#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time

sys.path.append("/home/pi/apps/libs")
from Adafruit_BMP085 import BMP085

# GY-65 (BMP085)

def readPressure(addr=0x77):
	bmp = BMP085(addr)
	
	Pressure = bmp.readPressure() / 100.0
	Altitude = bmp.readAltitude()
	Temperature = bmp.readTemperature()
	
	return Pressure, Temperature, Altitude

if __name__ == "__main__":
	print "GY-65 Pressure & Temperature sensor"

	try:
		addr= sys.argv[1]
	except:
		print "Using default address"
		addr="0x77"

	print "Reading data from addr=" + addr
	print "(hPa, ºC, m)"

	print readPressure(int(addr,16))