

import random # we will be using the random func for computer nums
winning_nums = [9,44,4,9,13,7,24] # winning nums 

wins = 0
losses = 0

def pick6():
    comp_6 = [] 
    for _ in range(0, 6):
        comp_6.append(random.randint(0, 99))
    return comp_6   #creating function to pick 6 
for i in range(100_000):    
    compnums = pick6()

    
    for i in range(6):
        if winning_nums[i] == compnums[i]:
            
            wins += 1 
        else:
            
            losses += 1

print(f"The computer won {wins} this many times and lost {losses} this many times ")
var = var1 #test line 
