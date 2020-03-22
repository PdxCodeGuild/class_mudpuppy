
# Lab 6: Password Generator
"""
Let's generate a password of length `n` using a `while` loop and `random.choice`, this will be a string of random characters.
"""
import random
import string

# string._file_ = random.choice('string.ascii_letters + string.punctuation + string.digits')
# #print((string._file_))

# pass_num = input ("How many characters? ")
# pass_num = int(pass_num)
# out_num = ''

# for piece in range(pass_num):
#         out_num = out_num + random.choice(string.ascii_letters + string.punctuation + string.digits)
# print(out_num)

string._file_ = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)


pass_low = input("How many lowercase? ")
pass_low = int(pass_low)

pass_high = input("How many uppercase? ")
pass_high = int(pass_high)

pass_dig = input("How many numbers? ")
pass_dig = int(pass_dig)

out_num = ''
for piece in range(pass_low):
    out_num = out_num + random.choice(string.ascii_lowercase)
for piece in range(pass_high):
    out_num = out_num + random.choice(string.ascii_uppercase)
for piece in range(pass_dig):
    out_num = out_num + random.choice(string.digits)

print(out_num)
