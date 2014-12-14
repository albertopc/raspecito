#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import RPi.GPIO as GPIO

def readMotion(pin=17):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.IN)
	return GPIO.input(pin)

if __name__ == "__main__":
	print "PIR Module - Motion detection"

	try:
		pin= sys.argv[1]
	except:
		print "Using default pin"
		pin="17"

	print "Reading data from pin=" + pin
	print "(Boolean)"
	
	print readMotion(int(pin))