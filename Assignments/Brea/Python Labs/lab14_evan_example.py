#Evan's example for Lab 14
import random

def pick6():
    ticket = []
    for _ in range(6):
        ticket.append(random.choice(range(1, 100)))
        return ticket

def num_matches(user_ticket, winning_ticket):
    matches = 0
    for i in range(len(user_ticket)):
        if user_ticket[i] == winning_ticket[i]:
            matches += 1
        return matches

def get_winnings(matches):
    if matches == 0:
        return 0
    if matches == 1:
        return 4
    elif matches == 2:
        return 7
    elif matches == 3:
        return 100
    elif matches == 4:
        return 50000
    elif matches == 5:
        return 1000000
    elif matches == 6:
        return 25000000
    else:
        print("Error, got more matches than expected")

winning_ticking = pick6()

balance = 0

for _ in range(100000):
    user_ticket = pick6()
    balance -= 2

    matches = num_matches(user_ticket, winning_ticking)

    balance += get_winnings(matches)

print(balance)

