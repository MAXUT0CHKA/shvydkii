import RPi.GPIO as gpio

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT, initial = 0)
gpio.setup(troyka, gpio.OUT, initial = 1)
gpio.setup(comp, gpio.IN)


def dec2bin(a):
    s = []
    for i in range(7, -1, -1):
        if 2**i > a:
            s.append(0)
        else:
            s.append(1)
            a -= 2**i
    return s


def volt(num, dac):
    for i, j in enumerate(dec2bin(num)):
        gpio.output(dac[i], j)


def adc(dac, comp):
    for i in range(255):
        volt(i, dac)
        if not gpio.input(comp):
            return 3,3*i/255

try:
    while True:
        print(adc(dac, comp))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
