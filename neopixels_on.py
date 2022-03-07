import board
import neopixel
pixels = neopixel.NeoPixel(board.D18,12)

# light 1 pixel
#pixels[0] = (0, 0, 0)

#light all pixels
pixels.fill((110, 90, 65)) #for thin plastic

#pixels.fill((160, 130, 80)) # for thick glass

#lights off
#pixels.fill((0, 0, 0))
