import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

GPIO.output(26, 0)
time.sleep(2)
print("0")

try:
    while True:
      GPIO.output(26, 1)
      print("1")
      time.sleep(2)

      GPIO.output(26, 0)
      print("0")
      time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
