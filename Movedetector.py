#!/bin/bash/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR = 17
GPIO.setup(PIR, GPIO.IN)         #Read output from PIR motion sensor
i = 0

time.sleep(10)

while i==0:
    i=GPIO.input(PIR)
    
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        time.sleep(0.5)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        time.sleep(0.5)
        
