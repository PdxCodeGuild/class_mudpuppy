#Lab 13, version 2 taking capitals into account March 30th, 2020

import string

user_input = input("What secret message would you like to encode? : ")

# user_input = user_input.lower()

rot_input = int(input("How many rotations would you like to include? : "))

message_list = []

message_list[0:] = user_input

alpha_list = 'abcdefghijklmnopqrstuvwxyz'

cap_alpha_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

nums_list = '0123456789'

secret_message_list = []

for letter in message_list:    #convert letters of message into indices
    if letter in '!@#$%^&*().,?\' ': 
        secret_message_list.append(letter)

    if letter in alpha_list:
        num = alpha_list.index(letter)
        num += rot_input
        secret_message_list.append(alpha_list[num % 26])

    if letter in cap_alpha_list:
        num = cap_alpha_list.index(letter)
        num += rot_input
        secret_message_list.append(cap_alpha_list[num % 26])
    
secret_message = ''.join(secret_message_list)

print(f"Your secret message code is: {secret_message} ")
