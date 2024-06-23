from time import sleep
from inventor import NUM_LEDS
from breakout_bme68x import STATUS_HEATER_STABLE





def print_sensor_data(t, g, he):
    """Prints neatly formatted data, 'read_sensor_data()' must be called before"""
    print(f"Temperature: {t:.1f}C \tAir quality: {g:.1f} Ohms \tHeater: {he}")
    


def blinking_speed(gs):
    """Based on the gas measurement, increase or decrease the speed of the blinking pattern"""
    value = gs/1000
    if value < 25:
        sleep_cnst = .2
    elif 25 <= value < 50:
        sleep_cnst = .5
    elif 50 <= value < 75:
        sleep_cnst = 1
    elif 75 <= value:
        sleep_cnst = 1.5
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
    


## COLOURS rgb format
red_r, red_g, red_b = 255, 0, 0
orange_r, orange_g, orange_b = 249, 154, 14
green_r, green_g, green_b = 0, 255, 0
blue_r, blue_g, blue_b = 0, 0, 255
purple_r, purple_g, purple_b = 255, 0, 255


def blink_temperature_leds(speed_function_blink, numleds, temp, board_instance):
    """Sets an amount of LED's (depending on numleds) on the inventor board into a blinking pattern,
    the colour depends on the temperature measured by the temperature sensor
    The blinking speed depends on 'blinking_pattern()' """
    # if numleds % 4 == 0:
    #     #set a certain amount of LEDs to one colour representing the humidity
    #     #the rest should be another colour
    # else:    
    if 23.00 <= temp < 25.00:
            for i in range(0, numleds):
                board_instance.leds.set_rgb(i, green_r, green_g, green_b)
    elif temp < 23.00:
        for i in range(0, numleds):
            board_instance.leds.set_rgb(i, blue_r, blue_g, blue_b)
    elif 25.00 <= temp < 27.00:
        for i in range(0, numleds):
            board_instance.leds.set_rgb(i, orange_r, orange_g, orange_b)
    elif 27.00 <= temp < 30.00:
        for i in range(0, numleds):
            board_instance.leds.set_rgb(i, red_r, red_g, red_b)
    elif 30.00 < temp:
        for i in range(0, numleds):
            board_instance.leds.set_rgb(i, purple_r, purple_g, purple_b)
    # IF THE AIR IS NOT POLLUTED, DON'T BLINK AT ALL
    sleep(speed_function_blink)
    if speed_function_blink != 1.5:
        for i in range(0, numleds):
            board_instance.leds.set_rgb(i, 0, 0, 0)
    sleep(speed_function_blink)
