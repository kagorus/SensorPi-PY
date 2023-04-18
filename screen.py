# Import the SSD1306 module.
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

import subprocess
import busio
import board
from board import SCL, SDA
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


# Screen Variables
page = 0
text = 255
bg = 0

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
