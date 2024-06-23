from time import sleep
from inventor import NUM_LEDS


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
    sleep(speed_function_blink)
    for i in range(0, numleds):
        board_instance.leds.set_rgb(i, 0, 0, 0)
    sleep(speed_function_blink)


def rainbow(board_instance):
    VALUE = 1.0
    BRIGHTNESS = 0.8
    DELAY = .05
    # Update each LED in turn to create a rainbow
    for i in range(NUM_LEDS):
        hue = float(i) / NUM_LEDS
        board_instance.leds.set_hsv(i, hue, VALUE, BRIGHTNESS)
        sleep(DELAY)
    board_instance.leds.clear()
    sleep(DELAY*2)


def end_loop(board_instance, time_list):
    """Compares the last two items of the given list, which
    stores the time difference between the user_button clicks.
    If the interval is small enough, it breaks the loop and turns
    all LED's off"""
    if (time_list[-1] - time_list[-2]) < 1000:
        board_instance.leds.clear()
        for i in range(3):
            rainbow(board_instance)
        print("\nSee ya!\n")
        return 1
    else:
        return 0
    


