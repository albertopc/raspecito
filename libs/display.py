#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time

sys.path.append("/home/pi/apps/libs")
import Adafruit_SSD1306

import Image
import ImageDraw
import ImageFont

### Init display

# Raspberry Pi pin configuration:
RST = 24

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Load default font.
font = ImageFont.load_default()

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

def display_text(x,y,text):
	# Write two lines of text.	
	draw.text((x, y), text,  font=font, fill=255)

	# Display image.
	disp.image(image)
	disp.display()
	
if __name__ == "__main__":
	print "OLED 128x32 display test"
	display_text(2,2,"This is a test")
	time.sleep(0.5)
	display_text(2,14,"Hello World!")
