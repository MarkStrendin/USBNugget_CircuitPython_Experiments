import board
from board import *
import busio
from digitalio import DigitalInOut, Pull
import displayio
import adafruit_framebuf
import adafruit_displayio_sh1106
import adafruit_display_text
from adafruit_display_text import label
import terminalio

# Set up display
displayio.release_displays()
WIDTH = 130
HEIGHT = 64
BORDER = 1
i2c = busio.I2C(SCL, SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT)



# Initialize Image
def DisplayImage(IMAGE):
	bitmap = displayio.OnDiskBitmap(IMAGE)
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader) 
    group = displayio.Group()
    group.append(tile_grid) 
    display.show(group) 

#text = "Hello world"
#text_area = label.Label(terminalio.FONT, text=text)
#text_area.x = 0
#text_area.y = 0
#display.show(text_area)

# Main graphics loop
while True:
    DisplayImage("/faces/menu.bmp")
  