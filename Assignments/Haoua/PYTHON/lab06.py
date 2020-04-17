import random
import string
# import string
# import random

password = ""
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
characters = letters + digits + punctuation

user = int(input("how many characters would you like?"))

for i in range(user):
    password +=random.choice(characters)
print(password)

'''
Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters 
they'd like in their password. Generate a password accordingly.
'''
# pass1 = int(input("How many characters would you like? :"))
# lcase = int(input("How many lowercase letters would you like? :"))
# ucase = int(input("How many uppercase letters would you like? :"))
# numbers = int(input("How many numbers would you like? :"))
# special = int(input("How many special characters would you like? :"))

# # response = str(input("Would you like us to generate a password for you?"))

# # poss_res = ['yes', 'yeah', 'y', 'yah', 'yeah', 'for sure', 'sure', 'definitely', 'si']

# password = ""
# letters = string.ascii_letters
# digits = string.digits
# punctuation = string.punctuation
# characters = letters + digits + punctuation
# for i in letters:
#     password += i 
# print(password)

# for i in digits:
#     password += i
# print(password)

# for i in punctuation:
#     password +=i
# print(password)

# for i in range(f'{user}'):
#     password +=random.choice(letters + digits + punctuation)
# # if  in poss_res:
# #     password += random.choice(characters)
# #     print(password)

# # user = input(f"Create a password (must be atleast {pass1} characters) : ")
# # len(user) == pass1

# # while True:
# #     if len(user) == pass1:
# #         print("Password successfully generated")
# #         break
# #     else:
# #         user = input("Please try again : ")
# #         continue
