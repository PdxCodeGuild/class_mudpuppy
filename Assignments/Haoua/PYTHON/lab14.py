'''Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance


Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
'''
import random

lottery_n =[]


for i in range (0,6):
    number = random.randint(1, 99)

    while number in lottery_n:
        number = random.randint(1, 99)
    lottery_n.append(number)


lottery_n.sort()

user_n = []

for i in range(0,6):
    number_user = int(input("Enter a number between 1-99: "))
    # while number < 1 or number > 99:
    #     number = int(input("BETWEEN 1 & 99 STUPID"))
    user_n.append(number_user)
    user_n.sort()

print(">>>> Today's lottery numbers are: ")
print(lottery_n)
print(">>>>  Your Selections: ")
print(user_n)

counter = 0
# for number_user in lottery_n:
if number_user in lottery_n:
    counter += 1    
print("You have guessed "+ str(counter) + " number(s) correctly.")


balance = 0
ticket = 2
if counter < 1:
    balance = - ticket
    print("Too bad, you're out $2.00")
elif counter == 1:
    balance = 7 - ticket
    print("You win $5.00")
elif counter == 2:
    balance = 100 - ticket
    print("You win $98.00")
elif counter == 3:
    balance = 50,000 - ticket
    print("You win $49,998.00")
elif counter == 4:
    balance = 1,000,000 - ticket
    print("You win $999,998.00")
elif counter == 5:
    balance = 25,000,000 - ticket
    print("You win $24,999,998.00")
else:
    print("please retry")

print("Your account balance is now: " +"$"+ "{:.2f}".format(balance))