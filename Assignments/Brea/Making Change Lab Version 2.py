# Making change lab March 20th, 2020

user_input = input("How many pennies do you have?: ")

user_input = int(user_input)

user_quarters = user_input // 25

remainder_quarters = (user_input // 25) % 10

user_dimes = user_input % 25 // 10

user_nickels = user_input % 25 % 10 // 5

user_pennies = user_input % 25 % 10 % 5

print(f"You have enough pennies to trade for {user_quarters} quarters, {user_dimes} dimes, {user_nickels} nickels, and {user_pennies} pennies remaining")

