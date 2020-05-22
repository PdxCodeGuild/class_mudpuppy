#Test Examples May 5th, 2020

import random

# winning_ticket = []
# user_ticket = []

# winning_ticket = [(i, random.randint(1, 9)) for i in range(6)]

# user_ticket = [(i, random.randint(1,9)) for i in range(6)]





# class TicketGen:
#     def __init__(self, stop):
#         self.stop = stop
    
#     def __iter__(self):
#         place = 0
#         while place < self.stop:
#             yield user_ticket = [(i, random.randint(1,9)) for i in range(6)]
#             place += 1

# for user_ticket in TicketGen(5):
#     print(user_ticket)
#     print(winning_ticket)
#     print(set(user_ticket) & set(winning_ticket))

my_gen = (num for num in range(5))
next(my_gen)
print(my_gen)