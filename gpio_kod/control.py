import os
import sys
from time import sleep
import RPi.GPIO as rp


try:
    pin = int(sys.argv[1])
    value = int(sys.argv[2])
    rp.setmode(rp.BCM)
    rp.setwarnings(False)
except:
    print("  ..  hatali islem  ..  ")

def run(pin,value):
    rp.setup(pin,rp.OUT)
    if(value == 0):
        rp.output(pin,0)
        print(str(pin) + " numarali pin degeri => " + str(value))
    elif(value == 1):
        rp.output(pin,1)
        print(str(pin) + " numarali pin degeri => " + str(value))
    else:
        print("  ..  hatali deger girildi  ..  ")
        
try:        
    if(pin == 99):
        print("\n__________ toplu islem baslatildi __________\n")
        for i in range(27):
            run(i,value)
    else:
        run(pin,value)
except:
    print("  ..  bir hata olustu  ..  ")



