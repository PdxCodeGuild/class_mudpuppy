import random
import string

abc = list(string.printable)
pwd = ''
length = int(input('How long do you want the password? '))
counter = 0
while counter < length:
    pwd += random.choice(abc)
    counter += 1
print(f'Your password is: {pwd}')
