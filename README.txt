Hello everybody.

Hardware:
Inventor2040W
BME680 connected to the board via the i2c

main.py is meant to be run through thonny on the Inventor2040W board, connected with a micro-USB cable to the computer.
To run the program open it in thonny, select your inventor with the sensor mounted onto, press on the run icon. 
The program uses the onboard LEDs to display the temperature and the air pollution.
The data is aquired through the BME680 sensor. 

If the air is not polluted, the LEDs will make a non-blinking light.
Otherwise the faster they will blink, the more polluted is the air. 
There are 3 blinking stages + the non blinking stage.
Try to spray some perfume on a piece of paper and hold it next to the sensor, it will blink very fast.

Depending on the temperature the LEDs will have one of five colours:
blue = coldest
green = cold
orange = mid
red = warm 
purple = hot

Pressing on the User switch, you can select between four LED patterns. 
You have to keep the switch pressed until it switches to the next mode, because the program checks the switch status 
just once every iteration.

Once every 10 iterations the program prints the measured data, so you can compare the data with the colours and pattern, which you are seeing.
After you have started the program let the sensor run for a couple of minutes, because the value of the gas fluctuates a lot in the beginning. 

You can end the program by pressing on the stop icon in thonny. 
Have fun!
