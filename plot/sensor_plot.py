import signal
import sys
import time

import adafruit_ads1x15.ads1015 as ADS
import adafruit_dht
import board
import busio
import plotext as plt
import RPi.GPIO as GPIO
from adafruit_ads1x15.analog_in import AnalogIn

# reading from GPIO 26
dht = adafruit_dht.DHT22(board.D26)

# setup adc
ads = ADS.ADS1015(busio.I2C(board.SCL, board.SDA))
ads.mode = ADS.Mode.SINGLE
ads.gain = 1
ads_chan = AnalogIn(ads, ADS.P0)

def draw():
    max_x = 100
    voltages = [0]
    temperatures = [0]

    zero_every_ten = 0

    while True:
        plt.clt()
        plt.clp()

        plt.plot(
            voltages,
            xside= "lower",
            yside = "left",
            label = "voltage"
        )
        plt.plot(
            temperatures,
            xside= "upper",
            yside = "right",
            label = "temperatures"
        )

        plt.sleep(0.1)
        plt.show()

        voltages.append(read_voltage(voltages[-1]))
        if len(voltages) > max_x or voltages[0] == 0:
            voltages.pop(0)

        if zero_every_ten == 0:
            temperatures.append(read_temp(temperatures[-1]))
            if len(temperatures) > max_x or temperatures[0] == 0:
                temperatures.pop(0)
        zero_every_ten = (zero_every_ten + 1) % 10

def read_temp(prev_value):
    try:
        return dht.temperature
    except RuntimeError as e:
        return prev_value

def read_voltage(prev_value):
    try:
        return ads_chan.voltage
    except RuntimeError as e:
        return prev_value

def handle_exit(sig, frame):
    print("exit")
    GPIO.cleanup()
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_exit)
    draw()
