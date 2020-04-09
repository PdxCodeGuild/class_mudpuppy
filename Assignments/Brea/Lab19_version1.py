#Lab 19, version 1, April 3rd, 2020

card_dict = {
'A': 1,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'J': 10,
'Q': 10,
'K': 10 }


while True: 
    card1_input = input("What is your first card? : ")
    if card1_input in card_dict.keys():
        break

while True:
    card2_input = input("What is your second card? : ")
    if card2_input in card_dict.keys():
        break
while True:
    card3_input = input("What is your third card? : ")
    if card3_input in card_dict.keys():
        break

def card_val(_str):
    num_val = card_dict[_str]
    return num_val

hand_val = card_val(card1_input) + card_val(card2_input) + card_val(card3_input)

def hit_again():
    hit_again_input = input("Would you like to draw another card? :")
    if hit_again_input == 'no':
        print("Thanks for playing!")
    if hit_again_input == 'yes':
        return next_card() #not sure what the right return is for here, I want it to bring up my next card function that collects the next card input

def next_card():
    next_card_input = input("What is your next card? :")
    next_card_input in card_dict.keys():
        hand_val = hand_val + card_dict[next_card_input]
        return hand_val


#Also, I'm not sure how to have the new hand_val after a 4th/5th/6th card iterates over these hand_val if statements. Do I make a loop?
if hand_val < 17:
    print(f"You have {hand_val} points.")
    hit_again() #want to use my hit_again function, but not sure how to print the input.

if hand_val >= 17 and hand_val < 21:
    print(f"You have {hand_val} points. I recommend you stay!")
    hit_again() #same as line 56

if hand_val == 21:
    print(f"You have {hand_val} points. Blackjack!")

if hand_val > 21:
    print(f"You have {hand_val} points. Already busted!")