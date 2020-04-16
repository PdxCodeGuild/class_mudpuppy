'''
Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjac
Over 21, advise "Already Busted

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
Then, figure out the point value of each card individually. Number cards are worth their number, 
all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Aces can be worth 11 if they won't put the total point value of both cards over 21.
Remember that you can have multiple aces in a hand. 
Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. 
For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
'''
 # q = int(input("How many cards do you have? : "))
# user_cards = input("What 3 cards do you have? : ")

# user_cards_list = []

# user_cards_list.append(user_cards)
#getting card data and inputting it into a list
user_cards_dict = {
    "J": 10,
    "K": 10,
    "Q": 10,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "A": 1
}

def cards():
    user_cards_list = [] #q = int(input("How many cards do you have? : "))
    for i in range(3):
    # q = int(input("How many cards do you have? : "))

        if i < 3: #i < q:
        # q = int(input("How many cards do you have : "))
            user_cards = input("What 3 card do you have?(Letters must be in Caps) : ")
            # user_cards.upper()
            #print(type(user_cards))
            user_cards_list.append(user_cards)
            #i += 1
            continue
        else: 
            print("Please try again")
    return user_cards_list
# cards()
# print(user_cards_list) #test to see if cards are being added to my list


# c2 = 2
# c3 = 3
# c4 = 4
# c5 = 5
# c6 = 6
# c7 = 7
# c8 = 8
# c9 = 9
# c10 = 10
# J = 10
# Q = 10
# K = 10
# A = 1
# A = 11

# print(type(c8))

# total = 0
max_total = 21

def points(user_cards_list):
    total = 0
    # max_total = 21
    if "J" in user_cards_list:
        total += 10
    if "Q" in user_cards_list:
        total += 10
    if "K" in user_cards_list:
        total += 10
    if "A" in user_cards_list and total > 10:
        total += 1
    if "A" in user_cards_list and total < 10:
        total += 11
    if "2" in user_cards_list:
        total += 2
    if "3" in user_cards_list:
        total += 3
    if "4" in user_cards_list:
        total += 4
    if "5" in user_cards_list:
        total += 5
    if "6" in user_cards_list:
        total += 6
    if "7" in user_cards_list:
        total += 7
    if "8" in user_cards_list:
        total += 8
    if "9" in user_cards_list:
        total += 9
    if "10" in user_cards_list:
        total += 10
    # else:
    #     print("Try some other shit I can't fix this code")
    return total

# print(type(points()))
# points()
# print(points())
# print(total) #test to see if total is being read, it is not.

#blackjack or nah checker
def blackjack(total):
    if total < 17:
        print("HIT")
    #break
    elif total >= 17 and total < max_total:
        print("Stay")
    #break
    elif total == max_total:
        print("BLACKJACK!!!!!!!!")
    #break
    elif total > max_total:
        print("Already bussssssteddd")
    #break
    else:
        print("Please try again later")
    #break
    print(total)
blackjack(points(cards())) #points = total essentially
