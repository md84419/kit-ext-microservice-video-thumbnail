#!/usr/bin/python
# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,broad-except
# pylint: disable=unused-import,attribute-defined-outside-init

"""Performs requests to the Google Maps Directions API."""

import carb
import logging
from logging import Logger

from fastapi import Body, Path, Query, FastAPI, HTTPException
import omni.ext
from omni.services.core import main
# import omni.usd

# PRODUCT_NAME = 'service-video-thumbnail'
VERBOSE = True

logger: Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
app: FastAPI = main.get_app()


# HTTP GET with body is non-standard.  We include it to make manual testing easier.
# See https://fastapi.tiangolo.com/tutorial/body/
@app.api_route('/ping2', methods=['get'], tags=['default'], include_in_schema=False)
@app.api_route('/ping2', methods=['post'], tags=['default'])
async def ping():
    return "OK"


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class RoboticaMicroserviceVideoThumbnailExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[robotica.service.video.thumbnail] robotica service video thumbnail startup")

    def on_shutdown(self):
        print("[robotica.service.video.thumbnail] robotica service video thumbnail shutdown")
