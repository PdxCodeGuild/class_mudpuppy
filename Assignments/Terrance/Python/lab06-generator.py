#lab06-generator.py


import string
import random#Create a string of characters
characters = string.ascii_letters + string.digits + string.punctuation#declare a password variable
variable = ""
#loop 10 times
for i in range(10):
#Pick random characters
    variable += random.choice(characters)
#Add random characters to Password
#variable = random.choice(variable)
#print the Password
print(variable)