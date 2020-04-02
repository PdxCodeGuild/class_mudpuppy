import random
from huepy import *


def _main_():
    how_many = int(input('How many emoticons do you want? '))
    list_of_emoticons = []
    seperator = red(' or ')
    for i in range(how_many):
        list_of_emoticons.append(make_face())
    print(seperator.join(list_of_emoticons))
    user_choice = int(input('Which one do you like best? (1,2,3..)'))
    print(list_of_emoticons[user_choice - 1])

def make_eyes():
    return random.choice(':;8X')

def make_nose():
    return random.choice('->^•')

def make_mouth():
    return random.choice('D|])(P')

def make_face():
    return make_eyes() + make_nose() + make_mouth()

_main_()
