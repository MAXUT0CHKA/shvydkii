import RPi.GPIO as gpio

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def binn(a):
    s = []
    for i in range(7, -1, -1):
        if 2**i > a:
            s.append(0)
        else:
            s.append(1)
            a -= 2**i
    return s

def cycle(a):
    if int(a) + 0.5 > a and 0 <= a < 255.5:
        return int(a)
    else:
        return int(a) + 1

try:
    s = input()
    while s != "q":
        if not s.isnumeric():
            print("Введено не числовое значение")
        else:
            s = int(s)
            if s < 0 or s > 255:
                print("Введите число от 0 до 255")
            else:
                print("Будет подано напряжение около:", str(3.3*s/255))
                gpio.output(dac, binn(s))
        s = input()

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
