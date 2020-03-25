# Making change lab advanced version 2 March 20th, 2020

user_input = input("How many much money do you have?: $ ")

user_input = float(user_input)

user_input = round(user_input * 100)

while True:

    user_dollars = user_input // 100

    user_quarters = round(user_input % 100 // 25)

    user_dimes = round(user_input % 25 // 10)

    user_nickels = round(user_input % 25 % 10 // 5)

    user_pennies = round(user_input % 25 % 10 % 5)

    print(f"You have enough money to for {user_dollars} dollars, {user_quarters} quarters, {user_dimes} dimes, {user_nickels} nickels, and {user_pennies} pennies remaining")

    user_input2 = input("Would you like to add or subtract money, or are you done?: ")
    
    if user_input2 == 'add':
        user_input_add = input("How much would you like to add? : $ ")
        user_input_add = float(user_input_add)
        user_input_add = round(user_input_add * 100)
        user_input = user_input + user_input_add


    if user_input2 == "subtract":
        user_input_sub = input("How much would you like to subtract? : $ ")
        float(user_input_sub)
        user_input2 = round(user_input * 100)
        user_input = user_input + user_input_add

    if user_input2 == "done":
        print("Thank you!")
        break
