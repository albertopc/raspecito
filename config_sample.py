# -*- coding: utf-8 -*-

myLibs="/home/pi/apps/libs"

# Weather Station
thingspeak_wstation_key='X12345678901234X'
thingspeak_wstation_channel='X1234'

# PIR-Motion
thingspeak_pir_key='Y12345678901234Y'
thingspeak_pir_channel='Y1234'
pirPin=17
pirLedPin=24
pirCaptureFolder="/home/pi/apps/snapshots/"
pirCaptureFlagFile="/home/pi/apps/.captureImage"

# Raspecito Web
port=5001
username='myuser'
password='mypasswd'
captureImageFolder="/home/pi/apps/raspecitoWeb/static/snapshots/"
captureImageFlagFile=pirCaptureFlagFile

# RPi Monitor
thingspeak_rpimonitor_key='Z12345678901234Z'
thingspeak_rpimonitor_channel='Z1234'
