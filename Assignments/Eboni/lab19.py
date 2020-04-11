# card_dict = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
# card_choice1 = input("What is your first card? ")
# card_choice1 = card_dict[card_choice1]
# card_choice2 = input("What is your second card? ")
# card_choice2 = card_dict[card_choice2]
# card_choice3 = input("What is your third card? ")
# card_choice3 = card_dict[card_choice3]
# final_score = card_choice1 + card_choice2 + card_choice3
# if final_score <= 17:
#     print("Hit")
# elif final_score >= 17 and final_score < 21:
#     print("Stay")
# elif final_score == 21:
#     print("Blackjack!")
# elif final_score > 21:
#     print("Already Busted!")
"""
Version 2
"""
card_dict = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
# ace_counter = 0
# card_choice1 = input("What is your first card? ")
# if card_choice1 == 'Ace':
#     ace_counter += 1
# card_choice1 = card_dict[card_choice1]
# card_choice2 = input("What is your second card? ")
# if card_choice2 == 'Ace':
#     ace_counter += 1
# card_choice2 = card_dict[card_choice2]
# card_choice3 = input("What is your third card? ")
# if card_choice3 == 'Ace':
#     ace_counter += 1
# total = card_choice1 + card_choice2 + card_choice3
# print(total)
# print(total + 10)
# if ace_counter > 0 and total < 12:
#     total = total + 10
# print(total)

ace_counter = 0
cards = []
words = ["first", "second", "third"]
for i in range (3):
    card_choice1 = input(f"Choose your {words[i]} card: ")
    if card_choice1 == 'Ace':
        ace_counter += 1
    cards.append(card_choice1)
    card_choice1 = card_dict[card_choice1]

    # if card_dict[card_choice1] == 'Ace':
        # ace_counter += 10
        # print(sum(cards))


# for card_dict[i] in card_choice1:
#     card_choice1 = card_choice1 + 10
# print(sum(cards))


# for i in range(3):
#     if card_choice1 == 'Ace':
#         card_choice1 = card_choice1 + 10