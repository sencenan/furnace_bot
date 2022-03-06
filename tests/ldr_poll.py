import RPi.GPIO as GPIO
from time import sleep

DATA_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(DATA_PIN, GPIO.IN, GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(DATA_PIN):
            print("hi")
        else:
            print("lo")
        sleep(0.25)
except KeyboardInterrupt:
    print("clean up")
    GPIO.cleanup()
