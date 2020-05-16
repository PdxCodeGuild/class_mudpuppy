#lab14-pick_6.py

    # Generate a list of 6 random numbers representing the winning tickets
    # Start your balance at 0
    # Loop 100,000 times, for each loop:
    # Generate a list of 6 random numbers representing the ticket
    # Subtract 2 from your balance (you bought a ticket)
    # Find how many numbers match
    # Add to your balance the winnings from your matches
    # After the loop, print the final balance


def get_matches(user_ticket, winning_ticket):
    counter = 0
    for i in range(6):
        if user_ticket[i] == winning_ticket[i]:
            counter += 1
    return counter

import random

ticket_number = list(range(0,99))
winning_ticket = []
for piece in range(0, 6):
    winning_ticket.append(random.choice(ticket_number))

user_ticket = []
for piece in range(0, 6):
    user_ticket.append(random.choice(ticket_number))
print(user_ticket, winning_ticket)

for i in range(100_000):
    num_matches = get_matches(user_ticket, winning_ticket)

evaluations = ['$0', '$4', '$7', '$100', '$50_000', '$1_000_000', '$25_000_000']
print(f"You won {evaluations[num_matches]}")