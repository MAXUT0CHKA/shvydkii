import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(a):
    s = []
    for i in range(7, -1, -1):
        if 2**i > a:
            s.append(0)
        else:
            s.append(1)
            a -= 2**i
    return s

try:
    t = float(input())
    n = int(input())
    for i in range(n):
        for i in range(256):
            gpio.output(dac, dec2bin(i))
            time.sleep(t)
        for i in range(255, -1, -1):
            gpio.output(dac, dec2bin(i))
            time.sleep(t)
    

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
