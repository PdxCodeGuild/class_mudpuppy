#Lab 16, version 1, Image Manipulation

from PIL import Image

img_mudpuppy = Image.open("sweet_mudpuppy.jpg")

width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]


        pixels[i, j] = (r, g, b)

img.show()