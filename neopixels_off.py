import board
import neopixel
pixels = neopixel.NeoPixel(board.D18,12)

# light 1 pixel
#pixels[0] = (0, 0, 0)

#light all pixels
#pixels.fill((230, 230, 150))

#lights off
pixels.fill((0, 0, 0))
