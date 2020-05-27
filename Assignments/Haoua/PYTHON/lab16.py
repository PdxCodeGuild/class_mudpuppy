from PIL import Image, ImageDraw
import colorsys
img = Image.open("PYTHON/abstract2.jpg")
width, height = img.size
pixels = img.load()


'''
for i in range(width):
    for j in range(height):
        r,g,b = pixels[i, j]

        y = int(0.299*r + 0.587*g + 0.114*b)
        pixels [i, j] = y, y, y 
        # your code here

        

img.show()
'''

#--------------------- Version 2 -------------------

'''
for i in range(width):
    for j in range(height):
        r,g,b = pixels[i,j]
        h,s,v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
# do some math on h, s, v
        h=float(r/255)
        s=float(g/255)
        v=float(b/255)

        r,g,b=colorsys.hsv_to_rgb(h,s,v)
        r=int(r*255)
        g=int(g*255)
        b=int(b*255)


        # if h == 1:
        #     h -= .4
        # elif h < 1:
        #     h +=.4
        # if s == 1:
        #     s==1
        # elif s < 1:
        #     s+=.4
        pixels[i,j] = (r,g,b)
img.show()

'''
#---------Version 3--------------------


width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner
'''
draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((100, 100), (300, 300)), fill="lightblue")
'''
# draw a line from x0, y0, x1, y1
# using the color pink
# color = (256, 128, 128)  # pink
# draw.line((0, 0, width, height), fill=color)
# draw.line((0, height, width, 0), fill=color)


circle_x = width/5
circle_y = height/2
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y), fill='lightgreen')


color = (256, 128, 128)  # pink
# draw.line((100, 100, 100, 0), fill=color)
draw.line((circle_x, circle_y, circle_x,-0), fill=color)
# draw.line((100, circle_x, circle_y,0), fill=color)
draw.line((0, circle_x, circle_y,100), fill=color)

img.show()