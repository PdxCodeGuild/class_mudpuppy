import random



def _main_():
    how_many = int(input('How many emoticons do you want? '))
    emoticon = ''
    for _ in range(how_many):
        emoticon = make_face()
        print(emoticon)

def make_eyes():
    return random.choice(':;8X')
    
def make_nose():
    return random.choice('->^•')
    
def make_mouth():
    return random.choice('D|])(P')
    
def make_face():
    return make_eyes() + make_nose() + make_mouth()

_main_()
