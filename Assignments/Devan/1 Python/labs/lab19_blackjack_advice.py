
card_deck = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,\
             '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

c1 = input("What's your first card? ")
c2 = input("What's your second card? ")
c3 = input("What's your third card? ")
c1 = card_deck[c1]
c2 = card_deck[c2]
c3 = card_deck[c3]
total = c1 + c2 + c3

if total < 17:
    print(f"{total}: Hit")
elif total >= 17 < 21:
    print(f"{total}: Stay")
elif total == 21:
    print(f"{total}: Blackjack!")
elif total > 21:
    print(f"{total}: BUSTED!")
