import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

while(1):

    GPIO.output(11,True)

    time.sleep(0.5)

    GPIO.output(11,False)

    time.sleep(0.5)

GPIO.cleanup() 
