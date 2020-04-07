card_dict = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
card_choice1 = input("What is your first card? ")
card_choice1 = card_dict[card_choice1]
card_choice2 = input("What is your second card? ")
card_choice2 = card_dict[card_choice2]
card_choice3 = input("What is your third card? ")
card_choice3 = card_dict[card_choice3]
final_score = card_choice1 + card_choice2 + card_choice3
if final_score <= 17:
    print("Hit")
elif final_score >= 17 and final_score < 21:
    print("Stay")
elif final_score == 21:
    print("Blackjack!")
elif final_score > 21:
    print("Already Busted!")

