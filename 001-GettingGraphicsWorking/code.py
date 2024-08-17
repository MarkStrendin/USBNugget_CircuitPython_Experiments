import board
import busio
from digitalio import DigitalInOut, Pull
import displayio
import adafruit_framebuf
import adafruit_displayio_sh1106
import adafruit_display_text
import terminalio
import time

# Set up display
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=130, height=64)

# Initialize Image
def DisplayImage(IMAGE):
	bitmap = displayio.OnDiskBitmap(IMAGE)
	tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader) 
	group = displayio.Group()
	group.append(tile_grid) 
	display.show(group) 

time.sleep(.5)

# Main graphics loop
while True:
	DisplayImage("/faces/menu.bmp")
  