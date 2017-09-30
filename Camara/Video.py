#!/bin/bash/python3

from picamera import PiCamera
from os import system

camera=PiCamera()

camera.start_recording('video.h264')
camera.wait_recording(5)
camera.stop_recording()
h2mp4='MP4Box -add video.h264 video.mp4'        
system(h2mp4)        