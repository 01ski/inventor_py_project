from utime import sleep
from inventor import NUM_LEDS


def print_sensor_data(t, g, he, hu):
    """Prints neatly formatted data, 'read_sensor_data()' must be called before"""
    print(f"Temperature: {t:.1f}C \tHumidity: {hu:.1f}% \tAir quality: {g:.1f} Ohms \tHeater: {he}")


def rainbow(board_instance):
    """Displays a rainbow pattern on the LEDs"""
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
    """Compares the last three items of the given list, which
    stores the time difference between the user_button clicks.
    If the interval is small enough, it breaks the loop and turns
    all LEDs off. For three fast consecutive clicks, it ends the loop"""
    time_diff1 = time_list[-1] - time_list[-2]
    time_diff2 = time_list[-2] - time_list[-3]
    if (time_diff2 != 0) and (time_diff1 < 1000) and (time_diff2 < 1000):
        board_instance.leds.clear()
        for i in range(3):
            rainbow(board_instance)
        print(f"\n{'*'*10}\t See ya! \t{'*'*10}\n")
        return 1
    else:
        return 0    


def switch_function(time_list):
    """takes the times list as an argument, compares the last two
    items. If the gap is small enough, the function switches mode from 
    temperature to humidity mode or the opposite"""
    time_diff = time_list[-1] - time_list[-2]
    if time_diff < 1000 and time_diff != 0 :
        del time_list[-2:]
        return 1
    else: 
        return 0

    


