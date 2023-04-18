import sensors
import screen

import time
from datetime import datetime
from screen import *
from sensors import *





# Program Variables
timesRun = 0
firstRun = 1
triggerUpdate = 0

def draw_screen():
    if page == 0:
        global text
        global bg
        draw.rectangle((0, 0, width, height), outline=0, fill=bg)
        draw.text((x, top + 5), "Temp    : " + str(temperature_c) + "C | Last Read :", font=font, fill=text)
        draw.text((x, top + 20), "Humidity: " + str(humidity) + "%  |  " + current_time, font=font, fill=text)
        display.image(image)
        display.show()
        text = 255 if text == 0 else 0
        bg = 0 if bg == 255 else 255
        # print(f"Text: {text} bg: {bg}")

while True:
    try:
        if timesRun == 120 or firstRun == 1 or triggerUpdate == 1:
            timesRun = 0
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            # Draw a black filled box to clear the image.
            # draw.rectangle((0, 0, width, height), outline=0, fill=0)
            # Print the values to the serial port
            take_readings(current_time)
            
           # calls draw screen
            draw_screen()
            # draw.text((x, top + 5), "Temp    : " + str(temperature_c)+"C | Last Read :", font=font, fill=255)
            # draw.text((x, top + 20), "Humidity: " + str(humidity)+"%  |  "+ current_time, font=font, fill=255)
            # display.image(image)
            # display.show()
            timesRun = timesRun + 1
            firstRun = 0
        else:
            timesRun = timesRun + 1
            # print(f"Time{timesRun}")

    except RuntimeError as error:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0], current_time)
        timesRun = 120
        time.sleep(2.0)
        continue
    except Exception as error:
        dht_error()
        raise error

    time.sleep(0.5)
