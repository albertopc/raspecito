#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import datetime
import subprocess, re
from subprocess import Popen, PIPE

def captureImage(destin="/home/pi/"):
	print "Taking snapshot"
	now=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
	filename=destin+now+".jpg"
	args = ["fswebcam", "-r 1280x720", filename]
	proc = Popen(args, stdout=PIPE)
	out = proc.stdout.read()
	proc.stdout.flush()
	print out	
	return filename

if __name__ == "__main__":

	print "fswebcam taking snapshot..."
	
	print captureImage()
