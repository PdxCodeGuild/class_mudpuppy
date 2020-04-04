"""
Aces can be worth 11 if they won't put the total point value of both cards over 21.
Remember that you can have multiple aces in a hand.
Try generating a list of all possible hand values by doubling the number of values
    in the output whenever you encounter an ace.
For one half, add 1, for the other, add 11.
This ensures if you have multiple aces that you account for the full range of possible values.
"""

def find_card_value(card):
    if card == "A":
        return 1
    elif card == "J" or card == "Q" or card == "K":
        return 10
    return int(card)

def add_cards(c1, c2, c3):
    return c1 + c2 + c3

def blackjack_advisor():
    c1 = input("What's your first card? ").upper()
    c2 = input("What's your second card? ").upper()
    c3 = input("What's your third card? ").upper()

    total = add_cards(find_card_value(c1), find_card_value(c2), find_card_value(c3))

    if total < 17:
        print(f"{total}: Hit")
    elif total >= 17 < 21:
        print(f"{total}: Stay")
    elif total == 21:
        print(f"{total}: Blackjack!")
    elif total > 21:
        print(f"{total}: BUSTED!")


blackjack_advisor()
