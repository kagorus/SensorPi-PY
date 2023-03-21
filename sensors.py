import time
from datetime import datetime
import board
import adafruit_dht
from board import SCL, SDA
import subprocess
import busio
from PIL import Image, ImageDraw, ImageFont

# Import the SSD1306 module.
import adafruit_ssd1306
# font = ImageFont.load_default()
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
width = display.width
height = display.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

# Temp/ Humidity Readings
humidity = 0
temperature_c = 0

# Screen Variables
page = 0
text = 255
bg = 0

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
        print(f"Text: {text} bg: {bg}")


while True:
    try:
        if timesRun == 120 or firstRun == 1 or triggerUpdate == 1:
            timesRun = 0
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            # Draw a black filled box to clear the image.
            # draw.rectangle((0, 0, width, height), outline=0, fill=0)
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print(
                "Time: {} Raw: {}  Temp:  {:.1f} C    Humidity: {}%  Timer: {}s".format(
                   current_time, temperature_c, temperature_c, humidity, timesRun
                ))
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
        dhtDevice.exit()
        raise error

    time.sleep(0.5)
