#Lab 13, version 1, March 27th, 2020

import string

user_input = input("What secret message would you like to encode? : ")

message_list = []
message_list[0:] = user_input

rot_num = 13

alpha_list = 'abcdefghijklmnopqrstuvwxyz'

code_list = []          #list of indices for initial user_input message

rot_code_list = []      #list of +13 indices for message

secret_message_list = []

secret_message = ''

for letter in message_list:    #convert letters of message into indices
    code_list.append(alpha_list.index(letter))
    
for num in code_list:       #adds 13 to every code
    num += 13
    rot_code_list.append(num)

for num in rot_code_list:
    secret_message_list.append(alpha_list[num % 26])

secret_message = ''.join(secret_message_list)

print(f"Your secret message code is {secret_message} ")

