import random
import string

def randchoice(in_string):
    rand_0_1 = random.random()
    rand_0_len = rand_0_1 * len(in_string)
    rand_index = int(rand_0_len)
    return in_string[rand_index]

chars = string.ascii_letters + string.digits
password = ''
counter = 0
while counter < 10:
    password += randchoice(chars)
    counter += 1
print(password)
