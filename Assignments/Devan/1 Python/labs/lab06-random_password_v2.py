import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
special = string.punctuation
digit = string.digits
pwd = ''
print('We are going to generate a random password.\nTell me how many for each type of character.')
upperQty = int(input('How many UPPERCASE letters? '))
lowerQty = int(input('How many lowercase letters? '))
specialQty = int(input('How many special characters? '))
digitQty = int(input('How many digits? '))

for i in range(upperQty):
    pwd += random.choice(upper)
for i in range(lowerQty):
    pwd += random.choice(lower)
for i in range(specialQty):
    pwd += random.choice(special)
for i in range(digitQty):
    pwd += random.choice(digit)
pwd = list(pwd)
random.shuffle(pwd)
print(f"Your password is: {''.join(pwd)}")
