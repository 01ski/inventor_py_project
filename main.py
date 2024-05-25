"""This program is using the User switch on the Inventor2040W to switch between X ambient light modes.
The intensity and the blinking pattern of the light change in relation with the air temperature and humidity"""

from inventor import Inventor2040W
from machine import Pin
from time import sleep
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE
from pimoroni_i2c import PimoroniI2C




#initialize the board 
board = Inventor2040W()

#CNST
DELAY = 3

# Create a bme connected via i2c to breakout pins
PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
bme = BreakoutBME68X(i2c)

def read_sensor_data(sensor_instance):
    """remember to initialize board and sensor before calling this function
    This function reads sensor data to these global variables"""
    global temperature, pressure, humidity, gas, heater
    temperature, pressure, humidity, gas, status, *_ = sensor_instance.read()
    heater = "Stable" if status & STATUS_HEATER_STABLE else "Unstable"

def print_sensor_data(temp, pres, hum, gs, heat):
    """prints neatly formatted data, read_sensor_data() must be called before"""
    print(f"{temp:0.2f}c, {pres:0.2f}Pa, {hum:0.2f}%, {gs:0.2f} Ohms, Heater: {heat}")


# Until the User switch is not pressed, continue reading via bme.read() every DELAY:
while True:
    try:
        read_sensor_data(bme)
        print_sensor_data(temperature, pressure, humidity, gas, heater)
        sleep(DELAY)
    except KeyboardInterrupt:
        break





