
import random

winning_ticket = []
for piece in range(6):
    winning_ticket.append(random.randint(0, 99))
print(winning_ticket)
balance = 0
matches = 0
user_ticket = []
for piece in range(6):
    user_ticket.append(random.randint(0, 99))
user_ticket = winning_ticket
for i in range(6):
    print(i)
    print(user_ticket[i], winning_ticket[i])
    if user_ticket[i] == winning_ticket[i]:
        matches += 1


    # while balance < 100000:
        # a_ticket = []
        # print(a_ticket)
        # balance += 1


import random
balance = 0
matches = 0

def gen_ticket():
    out_ticket = []
    for _ in range(6):
        out_ticket.append(random.randint(0, 99))
    return out_ticket
def earnings(matches):
    if matches == 0:
        return 0
    elif matches == 1:
        return 4 #ditto
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
winning_ticket = gen_ticket()
user_ticket[0] = 5
winning_ticket[0]= 5
balance -= 2
for i in range(6):
    print(i)
    print(user_ticket[i], winning_ticket[i])
    if user_ticket[i] == winning_ticket[i]:
        matches += 1
balance = balance + earnings(matches)
print(balance)