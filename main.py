"""This program is using the User switch on the Inventor2040W to switch between X ambient light modes.
The intensity and the blinking pattern of the light change in relation with the air temperature and humidity"""

from inventor import Inventor2040W, NUM_LEDS
from machine import Pin
from time import sleep
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE
from pimoroni_i2c import PimoroniI2C




#initialize the board 
board = Inventor2040W()

#initialize led on Pico
pico_led = Pin("LED", Pin.OUT)
#CNST
DELAY = .2


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

def blink_temperature_leds(temp):
    if 20.00 <= temp < 25.00:
            for i in range(0, NUM_LEDS - 6):
                board.leds.set_rgb(i, green_r, green_g, green_b)
    elif 18.00 <= temp < 20.00:
        for i in range(0, NUM_LEDS -6):
            board.leds.set_rgb(i, blue_r, blue_g, blue_b)
    elif 25.00 <= temp < 27.00:
        for i in range(0, NUM_LEDS - 6):
            board.leds.set_rgb(i, orange_r, orange_g, orange_b)
    sleep(.2)
    for i in range(0, NUM_LEDS - 6):
        board.leds.set_rgb(i, 0, 0, 0)


## COLOURS
red_r, red_b, red_g = 255, 0, 0
orange_r, orange_g, orange_b = 249, 154, 14
green_r, green_g, green_b = 0, 255, 0
blue_r, blue_g, blue_b = 0, 0, 255


count = 0

while True:
    try:
        read_sensor_data(bme)
        if (count % 10) == 0:
            print_sensor_data(temperature, pressure, humidity, gas, heater)
        blink_temperature_leds(temperature)
        if heater == "Stable":
            pico_led.toggle()
        elif heater == "Unstable":
            pico_led.on()
        sleep(DELAY)
        count += 1
    except KeyboardInterrupt:
        board.leds.clear()
        pico_led.off()
        break





