# # VERSION 2 - ACE TO 11 DOESNT RUN PROPERY :
## Whats your first card?
## 4
## Whats your second card?
## A
## Whats your third card?
## 2
## 7
## Total in hand: 
## 7
## A: 
## 11
## Stay

# # VERSION 1

# import random
# cards_dict  =  { "K" : 10 , "Q" : 10 , "J" : 10 , "10" : 10 , "9" : 9 , "8" : 8 , "7" : 7 , "6" : 6, "5" : 5 , "4" : 4 , "3" : 3 , "2" : 2 , "A" : 1}
 
# # print(cards_dict.values())
 
# # print (cards_dict['K'])
 
# print("Whats your first card?")
 
# card_1 = random.choice(list(cards_dict))
 
# print(card_1)
 
# print("Whats your second card?")
 
# card_2 = random.choice(list(cards_dict))
 
# print(card_2)
 
# print("Whats your third card?")
 
# card_3 = random.choice(list(cards_dict))
 
# print(card_3)
# print(cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3))
 
# #all_ cards  =  cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) + cards_dict.get(card_4) + cards_dict.get(card_5) + cards_dict.get(card_6) + cards_dict.get(card_7) + cards_dict.get(card_8) + cards_dict.get(card_9) + cards_dict.get(card_10) + cards_dict.get(card_11)
 
# #current_hand =
 
#  #draw_card = add(random.choice(list(cards_dict)))
 


# if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) == 21:
#                 print("Blackjack")
# if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) < 17:
#            	print("Hit")
# #while cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) < 17:
#             	#add(random.choice(list(cards_dict)))                        	
# if 21 > cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) >= 17:
#                 print("Stay")
# if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) > 21:
#                 print("Busted")
 
 
 
 
# version 2:
import random
 
cards_dict  =  { "K" : 10 , "Q" : 10 , "J" : 10 , "10" : 10 , "9" : 9 , "8" : 8 , "7" : 7 , "6" : 6, "5" : 5 , "4" : 4 , "3" : 3 , "2" : 2 , "A" : 1}
 
# print(cards_dict.values())
 
# print (cards_dict['K'])
 
print("Whats your first card?")
 
card_1 = random.choice(list(cards_dict))
 
print(card_1)
 
print("Whats your second card?")
 
card_2 = random.choice(list(cards_dict))
 
print(card_2)
 
print("Whats your third card?")
 
card_3 = random.choice(list(cards_dict))
 
print(card_3)

user_sum = cards_dict[card_1] + cards_dict[card_2] + cards_dict[card_3]
print(user_sum)



print("Total in hand: ")

print(cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3))


if card_1 == 'A' or card_2 == 'A' or card_3 == 'A' :
    # a_in_hand = True 
    if user_sum <= 11: 
        user_sum += 10

print(user_sum)

print(f'A: ')
print(cards_dict["A"])
 
# if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) == 21:
#                 print("Blackjack")
# if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) < 17:
#             	print( "Hit" )
 
# if 21 > cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) >= 17:
#                 print("Stay")
# if cards_dict.get(card_1) + cards_dict.get(card_2) + cards_dict.get(card_3) > 21:
#                 print("Broken")
 

if user_sum == 21:
                print("Blackjack")
if user_sum < 17:
            	print( "Hit" )
 
if 21 > user_sum >= 17:
                print("Stay")
if user_sum > 21:
                print("Broken")
 