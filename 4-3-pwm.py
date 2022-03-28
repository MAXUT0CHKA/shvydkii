import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(22, gpio.OUT)

shim = gpio.PWM(22, 1000)
shim.start(0)

try:
    s = input()
    while s != "q":
        s = int(s)
        shim.start(s)
        s = input()
finally:
    shim.stop()
    gpio.output(22, 0)
    gpio.cleanup()
