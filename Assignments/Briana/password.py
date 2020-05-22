# import random
# import string 
# user_input = int(input("Pick a number, any number "))

# n = user_input

# alphabet = string.ascii_letters 
# digits = string.digits
# punctuation = string.punctuation
# characters = alphabet + digits + punctuation

# password = ''
# i = 0
# while i <= n:
# 	password += random.choice(characters)
# 	i = i + 1
# print(password)

import random
import string 

# user_input = int(input("Pick a number, any number (greater than or equal to 4 "))
lowercase_input = int(input(" How many lowercase letters would you like your password to include? "))
uppercase_input = int(input(" How many uppercase letters would you like your password to include? "))
number_input = int(input(" How many numbers  would you like your password to include? "))
special_input = int(input(" How many special characters would you like your password to include? "))


# n = user_input
lc = lowercase_input 
uc = uppercase_input
nu = number_input
sp = special_input




lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
# alphabet = string.ascii_letters 
digits = string.digits
punctuation = string.punctuation
characters = lowercase + uppercase + digits + punctuation

password = ''
i = 0
# while i <= (n-1):
while i <= (lc-1) :
	password += random.choice(lowercase)
	i += 1

i1 = 0
while i1 <= (uc-1) :
	password += random.choice(uppercase)
	i1 += 1


i2 = 0
while i2 <= (nu-1) :
	password += random.choice(digits)
	i2 += 1


i3 = 0
while i3 <= (sp-1) :
	password += random.choice(punctuation)
	i3 += 1
print(password)
new_password=list(password)
random.shuffle(new_password)
print(''.join(new_password))
# print(random.shuffle(list(password)))


# uc
# nu
# sp
# Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. Generate a password accordingly.