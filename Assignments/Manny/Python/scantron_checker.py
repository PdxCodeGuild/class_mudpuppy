import random

scantron_choices = ['a', 'b', 'c', 'd', 'e' ]
nephews_answers = []

for piece in range (0,5):
    nephews_answers = nephews_answers.append(random.choice(scantron_choices))

answer_sheet = []
counter = 0  
for piece in range(0,5):
    answer_sheet.append(random.choice(scantron_choices))
for i in range(5):
    if answer_sheet[i] == nephews_answers[i]:
        
        print("correct")
        counter += 1
    else:
        print("incorrect")    