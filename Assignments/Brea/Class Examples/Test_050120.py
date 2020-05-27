#Test Examples, May 1st, 2020

import random

class Ticket:
    def __init__(self):
        self.nums = [random.randint(1, 9) for i in range(6)]

winner = Ticket()
one_ticket = Ticket()
print(t1.nums)

for i in range(10):
    one_ticket = Ticket()
    matches = 0
    for i in range(len(winner.nums)):
        if winner.nums[i] == one_ticket.nums[i]:
            matches += 1
print(matches)

# def make_ticket():
#     output = []
#     for _ in range(6):
#         output.append(random.randint(1, 9))
#     return output

# t1 = make_ticket()
# t2 = make_ticket()

# matches = 0

# for i in range(len(t1)):
#     if t1[i] == t2[i]:
#         matches += 1
# print(t1, t2, matches, sep='\n')

