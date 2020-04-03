#Lab 16, version 1, Image Manipulation

from PIL import Image
import os

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
img_path = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sweet_mudpuppy.jpg'))

img_mudpuppy = Image.open(img_path)

width, height = img_mudpuppy.size
pixels = img_mudpuppy.load()

for i in range(width):
    for j in range(height):
        (R, G, B) = pixels[i, j]
       
        R = R * 0.299
        G = G * 0.587
        B = B * 0.114

        Grey = int(R + G + B)

        pixels[i, j] = (Grey, Grey, Grey)

img_mudpuppy.show()


Y = 0.299*R + 0.587*G + 0.114*B