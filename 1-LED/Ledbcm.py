import RPi.GPIO as GPIO  
import time

# blinking function

def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return

# to use Raspberry Pi board pin numbers  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(17,GPIO.OUT)  

# blink GPIO17 10 times
for i in range(0,10):  
        blink(17)  
GPIO.cleanup()   
