#import libraries
from picamera import PiCamera
import time
import board
import neopixel

#setup variables
interval = 280 #in s = 10min (60 sec) - 20s de stabi_delay
frame = 0
stabi_delay = 20 #in s time for LEDS to stabilize before pic to get similar lighting

#setup neopixels
pixel_pin = board.D18
num_pixels = 12
pixels = neopixel.NeoPixel(board.D18,12)
#pixels.fill((50, 50, 50))

#setup & start camera, & let it settle
camera = PiCamera()
#camera.resolution = (4056, 3040) #full res
#camera.resolution = (3840, 2160)
camera.resolution = (2800, 2800) 
time.sleep(2)

while (frame < 200):
	pixels.fill((110, 90, 65)) #WB otherwise blue dominant
	camera.start_preview()
	time.sleep(stabi_delay)
	camera.capture('/home/pi/Videos/220118-tl10/tl10a_%04d.jpg' % (frame))
	time.sleep(2)
	camera.stop_preview()
	pixels.fill((0, 0, 0))
	frame =  frame + 1
	time.sleep(interval)
