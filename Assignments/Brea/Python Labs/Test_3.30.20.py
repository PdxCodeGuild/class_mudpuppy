#Test for March 30th, 2020 Coding Class

#Scantron checker.py

import random

scantron_choices = ['a', 'b', 'c', 'd', 'e']    # = list('abcde')

def make_rand_answers():    #function version of choosing 
    out_answers = []
    for _ in range(5):
        out_answers.append(random.choice(scantron_choices)
        return out_answers

nephews_answers = make_rand_answers()
answer_sheet = make_rand_answers()
print(nephews_answers, answer_sheet)

counter = 0

# for piece in range(0, 5):
#     nephews_answers.append(random.choice(scantron_choices))

# answer_sheet = []
# for piece in range(5):
#     answer_sheet.append(random.choice(scantron_choices))

# print (nephews_answers, answer_sheet)

for _ in range(5):
    if answer_sheet[_] == nephews_answers[i]:
        print("Correct")
        counter += 1  #counter = counter + 1
    else:
        print("Incorrect")

print(f"Your nephew got {counter} correct answers")

evaluations = ['poor', 'mediocre', 'adequate', 'good', 'great']
print(f"This student did {evaluations[counter]}")

---
#Evan lecture

def caesar(str, shift):     # one way of doing the ROT13 lab
    encrypted_string = ''
    for char_code in str.encode('ascii')
        encrypted_string += chr((char_code + shift - 97) % 26 + 97)
    return encrypted_string


