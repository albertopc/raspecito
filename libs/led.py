#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import RPi.GPIO as GPIO

def ledSetup(pin=24):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	time.sleep(2)
	return True

def ledOn(pin=24):
	return GPIO.output(pin, True)

def ledOff(pin=24):
	return GPIO.output(pin, False)

if __name__ == "__main__":
	print "PIR Module - Motion detection"

	try:
		pin= sys.argv[1]
	except:
		print "Using default pin"
		pin="24"

	ledSetup(int(pin))

	print "Switching on pin=" + pin
	ledOn(int(pin))

	time.sleep(30)

	print "Switching off pin=" + pin
	ledOff(int(pin))

	GPIO.cleanup()
