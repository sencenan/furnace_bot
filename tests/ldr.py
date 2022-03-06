import signal
import sys
import RPi.GPIO as GPIO

DATA_GPIO = 26

def handleExit(sig, frame):
    print("exit")
    GPIO.cleanup()
    sys.exit(0)

def handler(channel):
    if GPIO.input(DATA_GPIO):
        print("hi-dark")
    else:
        print("lo-light")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DATA_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(DATA_GPIO, GPIO.BOTH, callback=handler, bouncetime=50)
    handler(DATA_GPIO)

    signal.signal(signal.SIGINT, handleExit)
    signal.pause()


