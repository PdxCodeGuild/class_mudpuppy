# Generate a list of 6 random numbers representing the winning tickets
# Loop 100,000 times, for each loop:
    # Generate a list of 6 random numbers representing the ticket
    # Subtract 2 from your balance (you bought a ticket)
    # Find how many numbers match
    # Add to your balance the winnings from your matches
    # After the loop, print the final balance
import random


def pick6():
    nums = [random.randint(1,99) for i in range(6)]
    return nums

def find_matches(winning_nums, ticket):
    jackpot = [0, 4, 7, 100, 50000, 1000000, 25000000]
    num_wins = 0
    for i in range(6):
        if winning_nums[i] == ticket[i]:
            num_wins += 1
    return jackpot[num_wins]

winning_nums = pick6()
cost = 0
earnings = 0
for i in range(1000000):
    ticket = pick6()
    cost += 2
    earnings += find_matches(winning_nums, ticket)

net_earnings = earnings - cost


print(f"Winning numbers are: {winning_nums}.")
print(f"You spent: ${cost}")

if net_earnings > 0:
    print(f"You made: ${net_earnings}")
else:
    print(f"You lost: ${net_earnings}")
