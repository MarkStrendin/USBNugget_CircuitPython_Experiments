import board
import busio
from digitalio import DigitalInOut, Pull
import displayio
import adafruit_framebuf
import adafruit_displayio_sh1106
import adafruit_display_text
import terminalio
import time

from adafruit_display_text import label

# Set up display
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=130, height=64)

MENU_ITEMS = ["One", "Two", "Three", "Four", "Five", "Six"]

def RenderMenu(SELECTEDINDEX):	
	font = terminalio.FONT

	# Set up menu image
	MENU_BITMAP = displayio.OnDiskBitmap("/faces/menu.bmp")
	MENU_BITMAP_TILEGRID = displayio.TileGrid(MENU_BITMAP, pixel_shader=MENU_BITMAP.pixel_shader) 
	MENU_X = 10
	MENU_Y_OFFSET = 10
	BITMAP_GROUP = displayio.Group()
	BITMAP_GROUP.append(MENU_BITMAP_TILEGRID)

	# Set up menu text
	MENU_TEXT_GROUP = displayio.Group()
	color = 0xFFFFFF

	# Menu items
	menu_item_count = 0
	for menu_item in MENU_ITEMS:		
		text_area = label.Label(font, text=menu_item, color=color)
		text_area.x = MENU_X
		text_area.y = MENU_Y_OFFSET + (menu_item_count * 10)
		MENU_TEXT_GROUP.append(text_area)
		menu_item_count=menu_item_count+1

	MAIN_SCREEN_GROUP = displayio.Group()
	MAIN_SCREEN_GROUP.append(BITMAP_GROUP)
	MAIN_SCREEN_GROUP.append(MENU_TEXT_GROUP)
	display.show(MAIN_SCREEN_GROUP)

menu_selected_index = 1
time.sleep(.5)

# Main graphics loop
#while True:
#DisplayImage("/images/cat_idle.bmp")

while True:
	RenderMenu(menu_selected_index)
	menu_selected_index=menu_selected_index+1
	time.sleep(3)

  