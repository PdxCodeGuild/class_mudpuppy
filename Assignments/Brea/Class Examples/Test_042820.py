#Test Files, April 28th, 2020

import random

class Cat:
    def __init__(self):
        self.color = random.choice(['orange', 'black', 'gray'])
        self.hunger = 0
        self.tired = 0
    
    def purr(self):
        print('purr')
        self.tired += 1

my_cat = Cat()
print(my_cat.color)
print(my_cat.tired)
print(my_cat.purr)
