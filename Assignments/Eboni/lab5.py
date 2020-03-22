"""
Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
"""

import random

eyes = ["%", ":", "!"]

noses = ["^", "*", "-"]

mouths = ["$", "&", "@"]

random_eyes = random.choice(eyes)
# print (random_eyes)

random_noses = random.choice (noses)
# print (random_noses)

random_mouths = random.choice (mouths)
# print (random_mouths)
print(random_eyes + random_noses + random_mouths)



