#Lab 14, version 1.py

import random

winner_card = []
my_card = []

def pick_six():
        card = []
        for _ in range(6):
            card.append(random.choice(range(1, 100)))
        return card

def num_matches(winner_card, my_card):
    matching_counter = 0
    for _ in range(len(winner_card)):
        if winner_card[_] == my_card[_]:
            matching_counter += 1
    return matching_counter

def winnings(matching_counter, my_balance):
    if matching_counter == 0:
        my_balance += 0
        return my_balance
    elif matching_counter == 1:
        my_balance += 4
        return my_balance
    elif matching_counter == 2:
        my_balance += 7
        return my_balance
    elif matching_counter == 3:
        my_balance += 100
        return my_balance
    elif matching_counter == 4:
        my_balance += 50000
        return my_balance
    elif matching_counter == 5:
        my_balance += 1000000
        return my_balance
    elif matching_counter == 6:
        my_balance += 25000000
        return my_balance
    else:
        print("Error, more matches than expected!")

winner_card = pick_six()

plays = 100000

my_balance = 0

for _ in range (plays):
    my_card = pick_six()
    my_balance -= 2

    matching_counter = num_matches(winner_card, my_card)

    #my_balance += winnings(matching_counter)
    my_balance = winnings(matching_counter, my_balance)

roi_calc = round((my_balance - (plays * 2)) /(plays * 2))

print(f"I won ${my_balance}! My ROI was ${roi_calc}")