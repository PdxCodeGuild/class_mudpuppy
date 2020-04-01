#Lab 14, version 1.py

import random

my_balance = 0

plays = 10

def pick_six(nums_picked=6):
        card = []
        for _ in range(nums_picked):
            card.append(random.choice(range(1, 100)))
        return card

winner_card = pick_six()
print(winner_card)

my_card = pick_six()
print(my_card)

def num_matches(card1, card2):
    matching_counter = 0
    for _ in range(6):
        if card1[_] == card2[_]:
            matching_counter += 1
    return matching_counter

for _ in range(plays):
    matching_counter = num_matches(winner_card, my_card)
    my_balance -= 2

    if matching_counter == 1:
        my_balance += 4
    if matching_counter == 2:
        my_balance += 7
    if matching_counter == 3:
        my_balance += 100
    if matching_counter == 4:
        my_balance += 50,000
    if matching_counter == 5:
        my_balance += 1,000,000
    if matching_counter == 6:
        my_balance += 25,000,000

roi_calc = (my_balance - (plays * -2)) /(plays * -2)

print(f"I won ${my_balance}! My ROI was ${roi_calc}")