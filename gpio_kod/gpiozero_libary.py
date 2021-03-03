from gpiozero import LED
from time import sleep

pin = LED("27")

for i in range(11):

    pin.on()

    sleep(0.5)

    pin.off()

    sleep(0.5)




