# scantron_checker.py
import random
scantron_choices = ['a', 'b', 'c', 'd', 'e'] 
# = list('abcde')
nephews_answers = []
for piece in range(0, 5):
    nephews_answers.append(random.choice(scantron_choices))

answer_sheet = []
for piece in range(0, 5):
    answer_sheet.append(random.choice(scantron_choices))
print(nephews_answers, answer_sheet)

counter = 0
for i in range(5):
    if answer_sheet[i] == nephews_answers[i]:
        print("Correct")
        counter += 1 # counter = counter + 1
    else:
        print("Incorrect")
print(counter)

evaluations = ['flunk', 'poor', 'mediocre', 'adequate', 'good', 'great']
print(f"This student did {evaluations[counter]}")