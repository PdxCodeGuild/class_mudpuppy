# pillow_example.py
from PIL import Image
import colorsys

my_img = Image.new('RGB', (256, 256)) #setting width and height of image
pixels = my_img.load()

for i in range(my_img.width): # go left to right
    for j in range(my_img.height): # go top to bottom
        pixels[i, j] = (255, 0, 0)
        '''at coordinate x=i, y=j
        set color to red=255, green=0, blue=0'''
        # to make it green, blue and turquoise
        '''
        pixels[i, j] = (0, i, j)
        '''
        # to make it red with a green bar
        '''
        if i <= 100:
            pixels[i, j] = (0, 255, 0)
        else:
            pixels[i, j] = (255, 0, 0)
        '''
my_img.show()
