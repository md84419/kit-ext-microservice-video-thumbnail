#!/usr/bin/python
# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,broad-except
# pylint: disable=unused-import,attribute-defined-outside-init

"""Performs requests to the Google Maps Directions API."""

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import logging
from logging import Logger
import tempfile


import omni.ext
from omni.services.core import main
# import omni.usd

from .video_thumbnail import extract_and_compile_frames


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


@app.post('/video/thumbnail', tags=['video-thumbnail'])
async def thumbnail(file: UploadFile = File(...)):

    temp_input_file = tempfile.NamedTemporaryFile(delete=False)
    temp_input_file.write(await file.read())
    temp_input_file.close()

    temp_output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.m4v')

    try:
        # video_bytes = await file.read()

        # input_video_path = io.BytesIO(video_bytes)

        # output_video_path = io.BytesIO()

        # Specify target resolution and number of frames
        target_resolution = (256, 256)
        num_frames = 256

        # Extract frames and compile into a new video
        extract_and_compile_frames(temp_input_file.name, temp_output_file.name, target_resolution, num_frames)
        video_bytes = temp_output_file.read()
        response = StreamingResponse(iter([video_bytes]), media_type="video/mp4")
        response.headers["Content-Disposition"] = 'attachment; filename="thumbnail.mp4"'
        return response
    finally:
        temp_input_file.close()
        temp_output_file.close()
        # temp_file.unlink()  # Use this for BytesIO, not for temporary files


class RoboticaMicroserviceVideoThumbnailExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        pass
        # print("[robotica.service.video.thumbnail] robotica service video thumbnail startup")

    def on_shutdown(self):
        pass
        # print("[robotica.service.video.thumbnail] robotica service video thumbnail shutdown")
