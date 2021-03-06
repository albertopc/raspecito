# -*- coding: utf-8 -*-
import os
import sys
import datetime

from flask import url_for, render_template
from flask import request, Response
from functools import wraps

import config

sys.path.append(config.myLibs)
from raspecitoWeb import raspecitoWeb
from ds18b20 import readTemperature
from gy30 import readLuminosity
from dht22 import readHumidity
from gy65 import readPressure
from hcsr501 import readMotion
from fswebcam import captureImage
from tools import *

#AUTH functions

def check_auth(username,password):
	if username==config.username and password==config.password:
		return True

def authenticate():
	return Response(render_template("error_401.html",
                           title='Home',
						   user='desconocido',
						   active=0
						),
		401,
		{'WWW-Authenticate': 'Basic realm="Raspecito Web requiere clave"'})

def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated

#MyAPP functions

@raspecitoWeb.route('/')
@raspecitoWeb.route('/index')
@requires_auth
def index():
    return render_template("index.html",
                           title='Home',
						   active="0"
   )

@raspecitoWeb.route('/wstation')
@requires_auth
def wstation():
	tData={
		'temperature':readTemperature(0)[0],
		'humidity':float(readHumidity()[0]),
		'pressure':readPressure()[0],
		'light':readLuminosity(),
		'presence':readMotion(),
		'now':datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	}
	
	return render_template("wstation.html",
		title='Weather Station',
		active="1",
		**tData
	)

@raspecitoWeb.route('/graficas', methods=["GET", "POST"])
@requires_auth
def graficas():
    tData={
    	'wstation_channel':config.thingspeak_wstation_channel,
    	'pir_channel':config.thingspeak_pir_channel,
    	'rpimonitor_channel':config.thingspeak_rpimonitor_channel,
    }

    return render_template("graficas.html",
                           title='Seguimientos',
						   active="2"+"."+request.args.get("type"),
						   type=request.args.get("type"),
						   **tData
						   )

@raspecitoWeb.route('/vigilancia', methods=["GET", "POST"])
@requires_auth
def vigilancia():
	snapshots=os.listdir(config.captureImageFolder)
	snapshots.sort()
	
	return render_template("vigilancia.html",
		title='Vigilancia',
		active="3",
		fotos=snapshots,
		capture=os.path.isfile(config.captureImageFlagFile),
		pir_channel=config.thingspeak_pir_channel
		)

@raspecitoWeb.route('/takeImage', methods=["GET", "POST"])
@requires_auth
def takeImage():
	snapshot_dir=config.captureImageFolder
	captureImage(snapshot_dir)
	return vigilancia()

@raspecitoWeb.route('/deleteImage', methods=["GET", "POST"])
@requires_auth
def deleteImage():
	snapshot_dir=config.captureImageFolder
	os.remove(snapshot_dir+request.args.get("id"))
	return vigilancia()

@raspecitoWeb.route('/captureOn', methods=["GET", "POST"])
@requires_auth
def captureOn():
	touch(config.captureImageFlagFile)
	return vigilancia()

@raspecitoWeb.route('/viewImage', methods=["GET", "POST"])
@requires_auth
def viewImage():
    return render_template("captura.html",
                           title='Capturas',
						   active="3",
						   id=request.args.get("id")
						   )

@raspecitoWeb.route('/captureOff', methods=["GET", "POST"])
@requires_auth
def captureOff():
	os.remove(config.captureImageFlagFile)
	return vigilancia()
	
@raspecitoWeb.route('/sysInfo', methods=["GET", "POST"])
@requires_auth
def sysInfo():
	tData={
		'now':datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
		'uptime':uptime(),
		'loadavg':loadavg()
	}

	return render_template("system.html",
							title='Sistema',
							active="4"+"."+request.args.get("type"),
							**tData							
	)

@raspecitoWeb.route('/about')
@requires_auth
def about():
	return render_template("about.html",
							title='Acerca de...',
							active="5"
	)
	
@raspecitoWeb.route('/admin', methods=["GET", "POST"])
@requires_auth
def admin():
	if request.args.get("type")=="sr":
		# Reboot
		reboot()

		return render_template("esperar.html",
			title='Esperar',
			active="4"+"."+request.args.get("type")
		)
	elif request.args.get("type")=="sw":
		# wake up home server
		wakeuphomeserver(config.homeserver_mac)

		return render_template("despertar.html",
			title='Despertar',
			active="4"+"."+request.args.get("type")
		)
	else:
		return True
