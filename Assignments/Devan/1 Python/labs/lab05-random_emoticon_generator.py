import random

eyes = [':', ';', '8', 'X']
nose = ['-', '>']
mouth = ['D', '|', 'P', ')', '(']
how_many = input('How many emoticons do you want? ')
how_many = int(how_many)
emoticon = ''
for i in range(how_many):
    emoticon = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
    print(emoticon)
