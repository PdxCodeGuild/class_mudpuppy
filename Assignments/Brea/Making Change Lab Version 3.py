# Making change lab version 3 March 20th, 2020

user_input = input("How many much money do you have?: $ ")

user_input = float(user_input)

user_input = round(user_input * 100)

user_dollars = user_input // 100

user_quarters = round(user_input % 100 // 25)

user_dimes = round(user_input % 25 // 10)

user_nickels = round(user_input % 25 % 10 // 5)

user_pennies = round(user_input % 25 % 10 % 5)

print(f"You have enough money to for {user_dollars} dollars, {user_quarters} quarters, {user_dimes} dimes, {user_nickels} nickels, and {user_pennies} pennies remaining")

