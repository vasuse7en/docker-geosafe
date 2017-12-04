# coding=utf-8
from __future__ import absolute_import

import ast
import sys
import os

__author__ = 'Rizky Maulana Nugraha <lana.pcfre@gmail.com>'
__date__ = '8/25/16'


# import geonode settings
from geonode.settings import *
this_settings = sys.modules[__name__]

try:
    # if using QGIS Server, import settings
    ogc_backend = os.environ.get('OGC_BACKEND', 'geonode.qgis_server')
    if ogc_backend == 'geonode.qgis_server':
        from core.qgis_server import update_settings
        update_settings(this_settings)
except ImportError:
    pass

try:
    # if using Geosafe, import settings
    use_geosafe = os.environ.get('USE_GEOSAFE', 'True')
    use_geosafe = ast.literal_eval(use_geosafe)
    if use_geosafe:
        from core.geosafe import update_settings
        update_settings(this_settings)
except ImportError:
    pass

try:
    # if using Fluentgrid, import settings
    use_fluentgrid = os.environ.get('USE_FLUENTGRID', 'True')
    use_fluentgrid = ast.literal_eval(use_fluentgrid)
    if use_fluentgrid:
        from core.fluentgrid import update_settings
        update_settings(this_settings)
except ImportError:
    pass    

# Loggers
if DEBUG:
    LOGGING["handlers"]["console"]["level"] = "DEBUG"

    LOGGING["loggers"]["geonode"] = {
        "handlers": ["console"],
        "level": "DEBUG",
    }
    LOGGING["loggers"]["geosafe"] = {
        "handlers": ["console"],
        "level": "DEBUG",
    }

try:
    # convert to list
    allowed_hosts = os.environ['ALLOWED_HOSTS']
    ALLOWED_HOSTS = ast.literal_eval(allowed_hosts)
except:
    pass

# Used when running test in development mode
TESTING = sys.argv[1:2] == ['test']
