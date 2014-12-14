#!venv/bin/python
# -*- coding: utf-8 -*-

import config
from raspecitoWeb import raspecitoWeb

raspecitoWeb.run(host='0.0.0.0',port=config.port,debug=True)
