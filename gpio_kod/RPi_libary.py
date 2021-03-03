import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(27,GPIO.OUT)


for i in range(0,11):
    
    GPIO.output(27,GPIO.HIGH)

    sleep(0.5)

    GPIO.output(27,GPIO.LOW)

    sleep(0.5)

    
GPIO.cleanup()
