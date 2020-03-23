user_amount = float(input('How much money do you have (ex. 1.25)? '))
user_amount = round(user_amount * 100)
dollars = user_amount // 100
quarters = user_amount % 100 // 25
dimes = user_amount % 100 % 25 // 10
nickles = user_amount % 100 % 25 % 10 // 5
pennies = user_amount % 5

print(
    f'I can give you {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies.')
