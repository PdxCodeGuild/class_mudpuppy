from PIL import Image
img = Image.open("flag.jpg")
img_size = ('RGB', (256, 256))
pixels = img.load()

for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        gray = int(0.299*r + 0.587*g + 0.114*b)
        pixels[i, j] = (gray, gray, gray )
red = 255
green = 0
blue = 0

if i <= 100:
    pixels[i, j] = (255, 0, 0)
else:
    pixels[i, j] = (255, 0, 0)
img.show()



 

