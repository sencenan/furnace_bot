import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) 
p.start(7.5)

time.sleep(0.5) 
p.stop()
GPIO.cleanup()
exit()
