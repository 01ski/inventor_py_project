from utime import sleep


def humidity_leds(humidity, board_instance):
    """Displays a pattern on the LED's depending on the air
    humidity"""
    leds = humidity//10
    for i in range(0, leds):
        board_instance.leds.set_rgb(i, 51, 255, 255)
        sleep(.07)
    sleep(1)        
    board_instance.leds.clear()