from PIL import Image
import os
import colorsys


print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
img_path = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sweet_mudpuppy.jpg'))

img_mudpuppy = Image.open(img_path)

width, height = img_mudpuppy.size
pixels = img_mudpuppy.load()

for i in range(width):
    for j in range(height):
        (r, g, b) = pixels[i, j]
       
        (h, s, v) = colorsys.rgb_to_hsv(r/255, g/255, b/255)  # colorsys uses colors in the range [0, 1]

        hue = h

        h = h / 2
        

        #r, g, b = colorsys.hsv_to_rgb(h, s, v)      # do some math on h, s, v
        # convert back to [0, 255]

img_mudpuppy.show()

# r = int(r*255)
# g = int(g*255)
# b = int(b*255)

#         Grey = int(R + G + B)


#         pixels[i, j] = (Grey, Grey, Grey)
