# boot.py -- run on boot-up
from machine import Pin
from time import sleep

pin_list = [2, 4, 35, 34, 36, 39, 22, 21, 18, 19, 23, 5, 13, 12, 14, 27, 16, 17, 25, 26]
print("Pins Initialisieren")
for pin in pin_list:
    Pin(pin, Pin.IN)
sleep(0.02)