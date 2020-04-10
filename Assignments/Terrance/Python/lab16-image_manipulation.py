#lab16-image_manipulation.py

from PIL import Image
img = Image.open("frenchie_image.jpg")
width, height = img.size
pixels = img.load()

#v1
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = int(0.299*r + 0.587*g + 0.114*b)

        pixels[i, j] = (Y, Y, Y)

#v2
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        h *= 1.5
        if h > 1:
            h = .08
        s *= 1.5 
        if s > 1:
            s = .08
        # v *= 1.5
        # if v > 1:
        #     v = .08
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        pixels[i, j] = (r, g, b)
img.show()