import random
import os


cards =[
    "2", "3", "4"< "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"
    "2", "3", "4"< "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"
    "2", "3", "4"< "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"
    "2", "3", "4"< "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"
#valid with or without a comma
]

def calc_hand(user_cards):
    sum = 0

    non_aces = [card for card in hand if card != 'A']
    aces = [card for card in hand if card == 'A']
    
    for card in non_aces: #check if card is a letter or number
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)

    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum

# cards =[
#     "2", "3", "4"< "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"
#     "2", "3", "4"< "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"
#     "2", "3", "4"< "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"
#     "2", "3", "4"< "5", "6", "7", "8", "9", "10", "A", "Q", "J", "K"
# #valid with or without a comma
# ]

# random.shuffle(cards) #shuffles the list in place

# dealer = []
player = 0

cards.pop #takes item from the list. removes it then returns it.

# player.append(cards.pop()) #puts one card onto the player
# dealer.append(cards.pop()) 
# player.append(cards.pop()) 
# dealer.append(cards.pop()) 
i = 0
for i in range(6): #gives the system an opportuniy to repeat over and over
    if i < 6:
        # os.system('cls' if os.name == 'nt' else 'clear')
        user_cards = input("What cards do you have? :")
    
        #cls windows or clear in linux
        continue
    else:
        print("We only accept 6 cards: ")


    os.system('cls' if os.name == 'nt' else 'clear')
    
player_score = calc_hand(player)
    # dealer_score = calc_hand(dealer)



def myfunction():
    if player < 17:
        print("HIT")
    elif player >= 17 and total < max_total:
        print("Stay")
    elif player == max_total:
        print("BLACKJACK!!!!!!!!")
    elif player> max_total:
        print("Already bussssssteddd")
myfunction()

#     # print('Dealer Cars: [{}] [?]'.format(dealer[0]))
# print("Your cards [{}] [{}]".format(']['.join(player), player_score))
#     # print("")

    # print("What would you like to do? ")
    # print('[1] Hit')
    # print('[2] Stand')
    # print("")
    # choice = input("Your choice: ")
    # print("")
    
    

    # if choice == '1':
    #     player.append(cards.pop())
    # elif choice == "2":
    #     while calc_hand(dealer) <= 17:
    #         dealer.append(cards.pop())
    