#import libraries
from picamera import PiCamera
import time
import board
import neopixel
from PIL import Image, ImageOps, ImageEnhance 
import PIL

#setup variables
interval = 280 #in s = 10min (60 sec) - 20s de stabi_delay
frame = 0
stabi_delay = 8 #in s time for LEDS to stabilize before pic to get similar lighting

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

while (frame < 1000):
	pixels.fill((25, 22, 12)) #WB otherwise blue dominant
	camera.start_preview()
	time.sleep(stabi_delay)
	camera.capture('/home/pi/Videos/220317-lu/220317-lu_%04d.jpg' % (frame))
	time.sleep(2)
	camera.stop_preview()
	pixels.fill((0, 0, 0))
	
	#process
	img = Image.open('/home/pi/Videos/220317-lu/220317-lu_%04d.jpg' % (frame))
	img= ImageOps.grayscale(img)
	enhanceB = ImageEnhance.Brightness(img)
	img = enhanceB.enhance(1.2) #value between 0 and >1
	enhanceC = ImageEnhance.Contrast(img)
	#img = enhanceC.enhance(1.1) #value between 0 and >1
	img = img.save('/home/pi/Videos/processed/220317-lu-p_%04d.jpg' % (frame))
	
	frame =  frame + 1
	time.sleep(interval)
