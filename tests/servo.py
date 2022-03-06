import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) 
p.start(7.5)
time.sleep(1)

try:
    while True:
        s=7.5
        p.ChangeDutyCycle(s)
        time.sleep(1)
        print(s)

        s=5.5
        p.ChangeDutyCycle(s)
        time.sleep(1)
        print(s)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

