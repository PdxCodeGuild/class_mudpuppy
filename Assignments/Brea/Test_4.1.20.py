# # user_input = input(':').lower()
# # print(user_input)

# dictionary2 = {1: 'a', 2: 'b'}

# dictionary2[1] + input(':') + dictionary2[int(input('::'))] #we want this all to give us the same data type
# #string('a')     string('a')    int('2') that goes into dict to give 'b'
# 'aab'


#Learning DateTime
# import datetime

# now = datetime.datetime.today()
# print(now)

# my_birthday = "12-06-1988"
# my_birthday_datetime = datetime.datetime.strptime(my_birthday, "%m-%d-%Y") #turns string my_birthday int a datetime format

# print(my_birthday_datetime)

# my_bday = datetime.date(1988, 12, 6)

# #Day-name, Month-name Day-#, year...
# print(my_bday.strftime("%A, %B, %d, %Y"))

# message = "Brea was born on {:%A, %B %d, %Y}."
# print(message.format(my_bday))


#Learning to Do Lab 16, pillow_example.py
# from PIL import Image
# import colorsys

my_img = Image.new('RGB', (256, 256)) setting width and height of image
pixels = my_img.load()
pixels[0, 0] = (255, 0, 0)

for i in range(my_img.width): # go left to right
    for j in range(my_img.height): # go top to bottom
        pixels[i, j] = (0, i, j)
        if i <= 100:
            pixels[i, j] = (0, 255, 0)
        else:
            pixels[i, j] = (255, 0, 0)
        #at coordinates x=i, y=j set color to red 255, green 0, blue 0

my_img.show()

#print_board.py
board = []
board.append(['.', '*', 'X'])
board.append(['.', '*', 'X'])
board.append(['.', '*', 'X'])

for i in range(3):
    for j in range(3):
        print(board[i][j], end = '')
        print()