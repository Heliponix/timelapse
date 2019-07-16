#!/usr/bin/python

import time
import datetime
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PROX1 = 5
LED = 17

GPIO.setwarnings(False)

GPIO.setup(PROX1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
open = 1
closed = 0
state = open
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

while True:
	Reed1 = GPIO.input(PROX1)
	if Reed1 == closed and state == open:
		GPIO.output(LED, 1)
		print("switch closed")
		state = closed
		time.sleep(1)
		with picamera.PiCamera() as camera:
			camera.resolution = (2592, 1944)
			camera.vflip = True
			date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
			camera.start_preview()
			time.sleep(5)
			camera.capture("/media/exfat/TimeLapse6/"+ date +".jpg")
			print("Picture Taken")
			time.sleep(20)
		GPIO.output(LED, 0)
	elif Reed1 == open and state == closed:
		print("switch open")
		state = open
	time.sleep(5)
  
