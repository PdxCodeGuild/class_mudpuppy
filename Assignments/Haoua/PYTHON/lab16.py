from PIL import Image
img = Image.open("PYTHON/abstract2.jpg")
pixels = img.load()


Y = 0.299*R + 0.587*G + 0.114*B
for i in range(img.width):
    for j in range(img.height):
        pixels[i, j]=0.299, 0.587, 0.114


        # your code here

        

img.show()