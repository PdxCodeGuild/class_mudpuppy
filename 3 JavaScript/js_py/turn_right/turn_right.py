import random
directions = ['North', 'East', 'South', 'West']
start = random.randint(0, 3) # start = random.randrange(len(directions))
print('You are facing', directions[start])
user_turns = int(input("Turn right how many times? "))
end = start + user_turns
print('You are facing', directions[end % 4]) # print('You are facing', directions[end % len(directions)])
