import random

def main():
    winningNums = pick6()
    ticket = pick6()
    # testWin = [1,2,3,4,5,6]
    # testTik = [1,3,3,5,0,6]#should be 3 matches
    print('Winning Ticket: ', winningNums, '\n Ticket: ', ticket)
    num_matches(winningNums, ticket) 

def pick6():
    setList = list()
    for i in range(0, 6):
        setList.append(create_random_number())
    return setList
    
# Ticket   [1, 3, 3, 5, 0, 6]
# Winning  [1, 2, 3, 4, 5, 6] 

def num_matches(winning, ticket):
    trueMatches = 0
    for idx1, tickVal in enumerate(ticket):
        for idx2, winVal in enumerate(winning):
            if tickVal == winVal and idx1 == idx2:
                trueMatches += 1
    print('true matches found. \nNumber of matches = ', trueMatches)


def create_random_number():
    return random.randint(1,99)

if __name__ == '__main__':
    main()




