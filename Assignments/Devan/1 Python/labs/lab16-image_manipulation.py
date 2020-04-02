from PIL import Image, ImageDraw
import colorsys

img= Image.open("1 Python/labs/img/mudpuppy.jpeg")
width, height = img.size
pixels = img.load()


def greyscale():
    """ Converts an image to greyscale. """
    img_grey = img.convert('L')
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            if h < 0.5 or h > 0.9:
                s = 0

            r, g, b = colorsys.hsv_to_rgb(h, s, v)

            # convert back to [0, 255]
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            pixels[x, y] = (r, g, b)
    img_grey.save('1 Python/labs/img/mudpuppy_greyscale.jpeg')
    img_grey.show()



def stick_figure(width, height, head_color='tan'):
    """ Draws a stick figure using width, height, and head color. """
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # fill the background with color
    draw.rectangle(((0, 0), (width, height)), fill="grey")

    # draw a body, arms, legs
    color = (256, 128, 128)  # pink
    draw.line(((width/2), (height/4), (width/2), (height-(height/2.5))), fill=color) # body
    draw.line(((width/1.5), (height/2), (width-(width/1.5)), (height/2)), fill=color) # arms
    draw.line(((width/2), (height-(height/2.5)), (width/1.5), (height-(height/6))), fill=color) # l leg
    draw.line(((width/2), (height-(height/2.5)), (width-(width/1.5)), (height-(height/6))), fill=color) # r leg
    # draw a head
    circle_x = width/2
    circle_y = height/4
    circle_radius = width/10
    draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill=head_color)

    img.show()


stick_figure(600, 600, head_color='red')

# greyscale()
