# import string
# user_input = (input(f"Choose the first letter of your code "))
# user_input2 = (string.ascii_lowercase)
# code = (user_input2[0:13])
# code2 = (user_input2[13:26])
# full_code = code2 + code
# for letter in user_input:
#     print(letter)
# switch = (user_input2.index(letter))
# print(full_code[switch])

"""
version 2
"""

import string
user_input = (input(f"Choose the first letter of your code "))
user_input2 = (string.ascii_lowercase)
user_input3 = int(input(f"choose number of rotations: "))
user_input4 = (string.punctuation)
code = (user_input2[0:user_input3])
code2 = (user_input2[user_input3:26])
# print(code)
# print(code2)
full_code = code2 + code
for letter in user_input:
    print(letter)
switch = (user_input2.index(letter))
print(full_code[switch])



# my_str = 'abc'
# in_code = 'cab'
# output = ''
# for letter in in_code:
#     num = in_code.index(letter)
#     output = output + in_code[(num + 2) % 3]
# print(output)