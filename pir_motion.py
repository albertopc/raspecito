#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime
import RPi.GPIO as GPIO
import subprocess, re
from subprocess import Popen, PIPE

import config

sys.path.append(config.myLibs)
from hcsr501 import readMotion
from thingspeak import publishThingspeak
from led import *
from fswebcam import *

thingspeak_key = config.thingspeak_pir_key
PIR_PIN = config.pirPin
LED_PIN = config.pirLedPin
captureFolder = config.pirCaptureFolder
captureFlagFile = config.pirCaptureFlagFile

def my_callback(pin):
	time.sleep(1.5) # confirm movement by waiting 1.5 secs
	if GPIO.input(pin):
		print "Motion confirmed!"

		if os.path.isfile(captureFlagFile): 
			print "Capturing snapshot..."
			# Take a picture
			GPIO.output(LED_PIN, True)
			captureImage(captureFolder)
			GPIO.output(LED_PIN, False)

		# Update Thingspeak fields
		# Fields: PIR-1,2,3,4,5,6,7,8
		params=(1, "", "", "", "", "", "", "")
		publishThingspeak(thingspeak_key, params)

		# stop detection until 15 secs from detection
		print "Waiting..."
		GPIO.remove_event_detect(pin)
		time.sleep(13.5)
		GPIO.add_event_detect(pin, GPIO.RISING, callback=my_callback, bouncetime=500)
		print "Ready again..."
		

if __name__ == "__main__":

	print "Motion detection - PIR Modules (CTRL+C to exit)"

	try:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(LED_PIN, GPIO.OUT)
		
		time.sleep(2)
		print "Ready"
		
		GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=my_callback, bouncetime=500)

		while True:
			time.sleep(120)
			
			if GPIO.input(PIR_PIN)==0:
				print "No motion detected"
				params=(0,"","","","","","","")
				publishThingspeak(thingspeak_key,params)

	except KeyboardInterrupt:
		print "Quit"
		GPIO.cleanup()
