#lab05-emoticon.py

import random
eyes_list = ['8', 'X', '3', ':']
nose_list = ['>', '<', 'C', '-']
mouth_list = [')', '(', 'D', 'P']

for i in range(5):
    face = random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list)
    print(face)
