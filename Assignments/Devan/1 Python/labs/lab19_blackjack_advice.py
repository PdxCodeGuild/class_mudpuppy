

def blackjack_advisor():
    """ Ask's for 3 cards and tells you wether to stay or hit. """
    c1 = input("What's your first card? ").upper()
    c2 = input("What's your second card? ").upper()
    c3 = input("What's your third card? ").upper()

    possibles = find_possible_totals(find_card_value(c1), find_card_value(c2), find_card_value(c3))

    possibles.sort(reverse=True)    # Sorts the list largest to smallest
    total = [val for val in possibles if val <= 21] # Loops through totals and returns you the first possible total <= 21
    if len(total) == 0: # If there are no totals <= to 21, print bust
        print("You busted!")
        return
    total = total[0] # Grabs the value from the new total list
    if total < 17:
        print(f"{total}: Hit")
    elif total >= 17 > 21:
        print(f"{total}: Stay")
    elif total == 21:
        print(f"{total}: Blackjack!")
    elif total > 21:
        print(f"{total}: BUSTED!")


def find_card_value(card):
    """ Looks at input and returns a list of possible values for the card. """
    if card == "A":
        return [1, 11]
    elif card == "J" or card == "Q" or card == "K":
        return [10]
    return [int(card)]


def find_possible_totals(c1, c2, c3):
    """ Gives you a list of possible totals while looking at both values of Ace """
    possibles = []
    for val1 in c1:     # Looks at all each value of the card and adds them up
        for val2  in c2:
            for val3 in c3:
                possibles.append(val1 + val2 + val3)
    return possibles    # Returns a list of all possible totals

if __name__ == "__main__":
    blackjack_advisor()
