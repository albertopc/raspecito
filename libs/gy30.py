#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import smbus

# GY-30 functions

def readLuminosity(addr=0x23):
	bus = smbus.SMBus(1) #(512MB)
	# addr = 0x23 # i2c adress
   	data = bus.read_i2c_block_data(addr,0x11)
	return ((data[1] + (256 * data[0])) / 1.2)

if __name__ == "__main__":
	print "GY-30 Light sensor"

	try:
		addr= sys.argv[1]
	except:
		print "Using default address"
		addr="0x23"

	print "Reading data from addr=" + addr
	print "(lx)"

	print readLuminosity(int(addr,16))
