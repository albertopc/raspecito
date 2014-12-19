#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime
import subprocess, re
import pwd
import grp
from subprocess import Popen, PIPE
from datetime import timedelta

def touch(path,user="pi", group="pi"):
    with open(path, 'a'):
        os.utime(path, None)
	uid = pwd.getpwnam(user).pw_uid
	gid = grp.getgrnam(group).gr_gid
	os.chown(path, uid, gid)

		
def reboot():
	print "Launching command"
	args = ["sudo", "reboot", "-n"]
	proc = Popen(args, stdout=PIPE)
	out = proc.stdout.read()
	proc.stdout.flush()
	return True

def uptime():
	with open('/proc/uptime', 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
		uptime_string = str(timedelta(seconds = uptime_seconds))
		return uptime_string

def loadavg():
	return os.getloadavg()

if __name__ == "__main__":

	print "Nothing to do"
	
