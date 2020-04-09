card_dict = { 
"A" : 1 ,     
"K" : 10,
"Q" : 10,     
"J" : 10,
"10" : 10,     
"9" : 9,
"8" : 8,     
"7" : 7,
"6" : 6,     
"5" : 5,
"4" : 4,     
"3" : 3,
"2" : 2,     
"1" : 1,
}


   
while  var1 == "Yes":
    var1 = input("Blackjack advice continue Yes/No: ")
    card1 = input("Please input your first card:").upper()
    card2 = input("Please input your second card:").upper()

    user_total = card_dict.get(card1) + card_dict.get(card2)

    if user_total >= 17 and user_total <= 20:
        print("Stay")
    elif user_total == 21:
        print("Black Jack")

        while user_total < 17:
            print(f"Your {user_total} at should hit...")
            card = input("Please tell me your tell me another card: ").upper()
            user_total += card_dict.get(card)
            if user_total >= 17 and user_total <= 20:
                print("Stay")
            if user_total > 21:
                print("BUST!!!!!")
            elif user_total == 21:
                print("Blackjack") 
              
            
        