from PIL import Image, ImageDraw
import colorsys
from random import randint

img= Image.open("1 Python/labs/img/mudpuppy.jpeg")
width, height = img.size
pixels = img.load()


def greyscale(img):
    """ Converts an image to greyscale. """
    img_grey = img.convert('L')
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            if h < 0.1 or h > 0.9:
                s = 0

            r, g, b = colorsys.hsv_to_rgb(h, s, v)

            # convert back to [0, 255]
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            pixels[x, y] = (r, g, b)
    img_grey.save('1 Python/labs/img/mudpuppy_greyscale.jpeg')
    img_grey.show()


def gradient(img):
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    width, height = img.size
    gradient = Image.new('L', (width, 1), color=0xFF)
    for x in range(width):
        gradient.putpixel((x, 0), 255-x)
    alpha = gradient.resize(img.size)
    black_img = Image.new('RGBA', (width, height), color=0)
    black_img.putalpha(alpha)
    gradient_img = Image.alpha_composite(img, black_img)
    gradient_img.save('mudpuppy_gradient.png', 'PNG')



def stick_figure(width, height, head_color='tan'):
    """ Draws a stick figure using width, height, and head color. """
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    # fill the background with color
    draw.rectangle(((0, 0), (width, height)), fill="grey")
    # draw a head
    circle_x = width/2
    circle_y = height/4
    circle_radius = width/15
    draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill=head_color)
    color = ("tan")  # pink
    draw.line(((width/2), (height/4), (width/2), (height-(height/2.5))), fill=color, width=10) # body
    draw.line(((width/1.5), (height/2), (width-(width/1.5)), (height/2)), fill=color) # arms
    draw.line(((width/2), (height-(height/2.5)), (width/1.5), (height-(height/6))), fill=color) # l leg
    draw.line(((width/2), (height-(height/2.5)), (width-(width/1.5)), (height-(height/6))), fill=color) # r leg
    img.show()


def lines_1000():
    width = 500
    height = 500

    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    for i in range(1000):
        x0 = randint(0, width)
        y0 = randint(0, height)
        x1 = randint(0, width)
        y1 = randint(0, height)
        line_width = randint(1, 40)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

    img.show()

# lines_1000()
# stick_figure(400, 400)
greyscale(img)
# test(img)
