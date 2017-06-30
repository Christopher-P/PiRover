import picamera
import time
from datetime import datetime



camera = picamera.PiCamera()

camera.rotation = 180

camera.start_preview()

time.sleep(10)

camera.capture("Hello")
