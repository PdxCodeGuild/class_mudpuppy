import random

eyes = [':', ';', '8', 'X']
nose = ['-', '>']
mouth = ['D', '|', 'P', ')', '(']
how_many = input('How many emoticons do you want? ')
how_many = int(how_many)
emoticon = ''
list_of_emoticons = []
seperator = ' or '
for i in range(how_many):
    list_of_emoticons.append(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
print(seperator.join(list_of_emoticons))
user_choice = int(input('Which one do you like best? (1,2,3..)'))
print(list_of_emoticons[user_choice - 1])
