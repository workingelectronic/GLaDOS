#!/bin/bash/python3

import picamera

camera = picamera.PiCamera()
foto = camera.capture('photo.jpg')

