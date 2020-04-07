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

if hand_val < 17:
    print(f"You have {hand_val} points. Hit!")
elif hand_val >= 17 and hand_val < 21:
    print(f"You have {hand_val} points. Stay!")
elif hand_val == 21:
    print(f"You have {hand_val} points. Blackjack!")
elif hand_val > 21:
    print(f"You have {hand_val} points. Already busted!")