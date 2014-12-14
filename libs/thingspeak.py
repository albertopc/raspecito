#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import httplib, urllib

# Publish data into Thingspeak

def publishThingspeak(mykey, myfields):
	params = urllib.urlencode({'field1': myfields[0], 'field2': myfields[1], 'field3': myfields[2], 'field4': myfields[3], 'field5': myfields[4],'field6': myfields[5],'field7': myfields[6],'field8': myfields[7], 'key': mykey})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	print "Publishing...", response.status, response.reason
	data = response.read()
	conn.close()

if __name__ == "__main__":

	print "Thinspeak data publishing..."
	#params=("", "", "", "", "", "", "", "")
	#publishThingspeak(thingspeak_key, params)
	
	print "Nothing to publish..."
