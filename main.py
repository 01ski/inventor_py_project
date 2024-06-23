from inventor import Inventor2040W
from breakout_bme68x import BreakoutBME68X, STATUS_HEATER_STABLE
from pimoroni_i2c import PimoroniI2C
from machine import Pin
from utime import *
from module import *


#hardware initialization
board = Inventor2040W()
PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
bme = BreakoutBME68X(i2c)
pin = Pin(board.USER_SW_PIN, Pin.IN, Pin.PULL_DOWN)


#initialize variables for the readings, values are assigned inside of
#the 'read_sensor_data' function
temperature, gas, status, heater = None, None, None, None

def read_sensor_data(sensor_instance):
    """This function reads sensor data to the following global variables.
    Remember to initialize board and sensor before calling this function.
    Don't move this function to the module, or the global variables won't 
    work anymore.
    """
    global temperature, gas, status, humidity, heater
    data = sensor_instance.read()
    temperature, gas, status = data[0], data[3], data[4]
    heater = "Stable" if status & STATUS_HEATER_STABLE else "Unstable"

times = [0,1001]
times.append(ticks_ms())

#callback function of the interrupt 
def callback(pin):
    global user_switch_count, interrupt_status, times
    user_switch_count +=1
    interrupt_status = 1
    time = ticks_ms()
    times.append(ticks_ms())

#interrupt initialization         
pin.irq(trigger=pin.IRQ_FALLING, handler=callback)

#counters initialization
user_switch_count = 0
interrupt_status = 0
count_iterations = 0
lap = ticks_ms()


while True:
    try:
        read_sensor_data(bme)
        blink_temperature_leds(blinking_speed(gas), number_leds(user_switch_count), temperature, board)
        #print the sensor data just every 5th iteration
        if (count_iterations % 5) == 0:
            print_sensor_data(temperature, gas, heater)
        count_iterations += 1
        if end_loop(board, times):
            break
        
    except KeyboardInterrupt:
        board.leds.clear()
        break



    







