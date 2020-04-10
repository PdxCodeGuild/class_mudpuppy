#pattern_gen.py
import random
pattern_list = ['##', '%%', '@@', '//', '==', '\\\\]
length = int(input("How long? "))
for i in range(length):
    print(random.choice(pattern_list) *5)