#Test Files, April 10th, 2020

input_sentence = 'the quick brown fox...'

counter = {}

for letter in input_sentence:
    print(letter)
    if letter in counter:
        counter[letter] = counter[letter] + 1     #adds to counter value within counter dictionary
    else: 
        counter[letter] = 1
print(counter)

#---------------------------
#emotion_class_v2.py

import random
vowels = 'aeiouy'
e1 = random.choice(':;8') + random.choice('>-') + random.choice(')(/')
e2 = random.choice(':;8') + random.choice('>-') + random.choice(')(/')

def sunnies(in_emoticon): #takes in 
    return 'B' + in_emoticon[1] + in_emoticon[2]
    print(e1, sunnies(e1))

def __str__(self):  #allows self class to be represented as a string
    return self.eyes + self.nose + self.mouth

def __add__(self, other_em):
    '''returns a string of face parts randomly chosen from each emoticon'''
    return random.choice(self.eyes + other_em.eyes) + \
        random.choice(self.nose + other_em.nose) + \
        random.choice(self.mouth + other_em.mouth)


#------------------
def kid(in_e1, in_e2):  #takes in two emoticons, each emoticon with three things, leaves behind one emoticon
    return random.choice([in_e1[0], in_e2[0]]) + \
    random.choice([in_e1[1], in_e2[1]]) + \
    random.choice([in_e1[2], in_e2[2]])

print(e1, e2, sunnies(kid(e1, e2)))

#---------------------
#making a class
import random

class Emoticon:
    def __init__(self):     #init stands for initialize
        self.eyes = random.choice(':*;')
        self.nose = random.choice('>-~')
        self.mouth = random.choice('D(){}/\\')
    
    def sunnies(self):
        return 'B' + self.nose + self.mouth
    
e1 = Emoticon()
e1 = Emoticon()
print(e1, e2, e2.sunnies())
print(e1 + e2) #returns a string that represents a child