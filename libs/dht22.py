#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess, re
from subprocess import Popen, PIPE

# DHT-22
def readHumidity(type=2302, pin=25):
	start=time.time()
	
	args = ["sudo", "/home/pi/apps/libs/DHT", format(type), format(pin)]
	proc = Popen(args, stdout=PIPE)
	out = proc.stdout.read()
	proc.stdout.flush()

	temp = re.findall(r'[-]*[0-9]*.[0-9]* C', out)
	humi = re.findall(r'[-]*[0-9]*.[0-9]* %', out)

	if len(temp)>0 and len(humi)>0:
		temp = re.findall(r'[-]*[0-9]*.[0-9]*', temp[0])[0]
		humi = re.findall(r'[-]*[0-9]*.[0-9]*', humi[0])[0]
	else:
		time.sleep(0.5)
		if (time.time() - start) > 15:
			temp="0"
			humi="0"
		else:
			return readHumidity(type, pin)
	return humi, temp
	
if __name__ == "__main__":
	print "DHT-22 Humidity & Temperature Sensor"

	try:
		sensorType= sys.argv[1]
		sensorPin= sys.argv[2]
	except:
		print "Using default type"
		sensorType="2302"
		print "Using default pin"
		sensorPin="25"

	print "Reading data from a " + sensorType + " at pin=" + sensorPin
	print "(%, C)"
	
	print readHumidity(sensorType, int(sensorPin))
