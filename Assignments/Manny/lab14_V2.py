"""
    Generate a list of 6 random numbers representing the winning tickets
    Start your balance at 0
    Loop 100,000 times, for each loop:
    Generate a list of 6 random numbers representing the ticket
    Subtract 2 from your balance (you bought a ticket)
    Find how many numbers match
    Add to your balance the winnings from your matches
    After the loop, print the final balance
 """
import random
winning_ticket = random.choice(0,99)