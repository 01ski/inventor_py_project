"""This program is using the User switch on the Inventor2040W to switch between X ambient light modes.
The intensity and the blinking pattern of the light change in relation with the air temperature and humidity"""

from inventor import Inventor2040W, NUM_LEDS
from time import sleep
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE
from pimoroni_i2c import PimoroniI2C


#Already set some LEDs to change colour with the temperature measured by the bme680
#every 10 loops it prints the measurements of the sensor
#goal for today: create a blinking pattern dependent on the air quality

#hardware initialization
board = Inventor2040W()
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
    """prints neatly formatted data, 'read_sensor_data()' must be called before"""
    print(f"{temp:0.2f}c, {pres:0.2f}Pa, {hum:0.2f}%, {gs:0.2f} Ohms, Heater: {heat}")


def blinking_speed(gs):
    """Based on the gas measurement, increase or decrease the speed of the blinking pattern"""
    value = gs/1000
    if value < 50:
        sleep_cnst = .2
    elif 50 <= value < 75:
        sleep_cnst = .5
    elif 75 <= value < 100:
        sleep_cnst = 1
    elif 100 <= value:
        sleep_cnst = 5
    return float(sleep_cnst)


def number_leds(counter_press):
    """uses the count of the user switch presses to return the number of leds to be used
    in the 'blink_temperature_leds()"""
    if counter_press % 4 == 0:
        leds = NUM_LEDS - 6
    elif counter_press % 4 == 1:
        leds = NUM_LEDS
    elif counter_press % 4 == 2:
        leds = NUM_LEDS - 9
    elif counter_press % 4 == 3:
        leds = NUM_LEDS - 3
    return int(leds)
    

def blink_temperature_leds(speed_function_blink, numleds, temp):
    """Sets 6 of the 12 LED's on the inventor board into a blinking pattern,
    the colour depends on the temperature measured by the temperature sensor
    The blinking speed depends on 'blinking_pattern()' """
    if 20.00 <= temp < 25.00:
            for i in range(0, numleds):
                board.leds.set_rgb(i, green_r, green_g, green_b)
    elif 18.00 <= temp < 20.00:
        for i in range(0, numleds):
            board.leds.set_rgb(i, blue_r, blue_g, blue_b)
    elif 25.00 <= temp < 27.00:
        for i in range(0, numleds):
            board.leds.set_rgb(i, orange_r, orange_g, orange_b)
    elif 27.00 <= temp < 30.00:
        for i in range(0, numleds):
            board.leds.set_rgb(i, red_r, red_g, red_b)
    elif 30.00 < temp:
        for i in range(0, numleds):
            board.leds.set_rgb(i, purple_r, purple_g, purple_b)
    # IF THE AIR IS NOT POLLUTED, DON'T BLINK AT ALL
    if speed_function_blink != 5:
        sleep(speed_function_blink)
        for i in range(0, numleds):
            board.leds.set_rgb(i, 0, 0, 0)
        sleep(speed_function_blink)



## COLOURS
red_r, red_g, red_b = 255, 0, 0
orange_r, orange_g, orange_b = 249, 154, 14
green_r, green_g, green_b = 0, 255, 0
blue_r, blue_g, blue_b = 0, 0, 255
purple_r, purple_g, purple_b = 255, 0, 255

#initialize counters
count_iterations = 0
user_switch_count = 0

while True:
    try:
        read_sensor_data(bme)
        #print the sensor data just every 10th iteration
        if (count_iterations % 10) == 0:
            print_sensor_data(temperature, pressure, humidity, gas, heater)
        count_iterations += 1
        if board.switch_pressed():
            user_switch_count += 1
        blink_temperature_leds(blinking_speed(gas), number_leds(user_switch_count), temperature)
    except KeyboardInterrupt:
        board.leds.clear()
        break





