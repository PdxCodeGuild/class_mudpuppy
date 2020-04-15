 
#lab_19_blackjack.py
#Playing with number of cards and seeing what your socre 
   
def blackjack(cardstring):
    card_values = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }
    #converting to uppercase
    cards = str.upper(user_cards)
    # placing the value of each card into a list
    values = []
    for i in cards:
        if i in card_values:
            values.append(card_values[i])
    # getting a score
    score = sum(values)

    while score > 17:   
        # If score is over 17, checking to see if we can reduce an ace from 11 to 1 and still be in the game
        if 11 in values:
            score -= 10     
        else:
            print(f"You currenly have {score}. Bust!")
    if score == 17:
        print("Blackjack!")
    elif score < 17 and score >= 10:
        print(f"You currently have {score}. Stay.")
    elif score < 10:
        print(f"You currently have {score}. Hit.")

user_cards = input(
    "Enter your cards and this program will tell you if you should hit or not. (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K) ex: J2 ")

blackjack(user_cards)
