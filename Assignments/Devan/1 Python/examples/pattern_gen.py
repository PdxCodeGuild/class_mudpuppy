import random
pattern_list = ['##', '%%', '@@', '//', '==', '\\\\']
length = int(input('How long? '))
width = int(input('How wide? '))
counter = 0
while counter < length:
    print(random.choice(pattern_list) * width)
    counter = counter + 1
