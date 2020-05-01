#Test Examples April 24th, 2020

import string
import random

abc = string.ascii_lowercase
l1 = [abc]
l2 = list(abc)

print(l1)
print(l2)

l3 = []
l3 = [num for num in range(10)]
print(l3)

password = []
password2 = []
for i in range(10):
    password.append(random.choice(string.ascii_letters + string.punctuation + string.digits))
print(password)

password2 = [random.choice(random.choice(string.ascii_letters + string.punctuation + string.digits) for i in range(10)]
print(password2)