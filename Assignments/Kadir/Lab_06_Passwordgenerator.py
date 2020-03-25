#>>>Lab 6 Password Generator

'''Lab 6 Password Generator
Let's generate a password ten characters long using a loop (while loop or for
loop) and random.choice, this will be a string of random characters. '''

import random   

import string 

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
characters = letters + digits + punctuation


word = ""
for i in range(10):
    word += random.choice(digits)
print(word)

password = random.choice(lowercase)+random.choice(digits)+random.choice(punctuation)
print(password)





password = ""

user = int(input("how many characters would you like you your passord to be?"))

for i in range (user):
    password +=random.choice(characters)
print(password)

