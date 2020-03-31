# scantron_checker.py
import random
scantron_choices = ['a', 'b', 'c', 'd', 'e'] 

def make_rand_answers():
    out_answers = []
    for _ in range(0, 5):
        out_answers.append(random.choice(scantron_choices))
    return out_answers

nephews_answers = make_rand_answers()
answer_sheet = make_rand_answers()
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