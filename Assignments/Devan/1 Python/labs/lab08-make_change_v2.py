def make_change():
    user_amount = float(input('How much money do you have (ex. 1.25)? '))
    user_amount = round(user_amount * 100)
    if user_amount < 0:
        print('You must enter a positive number.')
    else:
        dollars = user_amount // 100
        leftover_pennies = user_amount % 100
        quarters = leftover_pennies // 25
        dimes = leftover_pennies % 25 // 10
        nickles = leftover_pennies % 25 % 10 // 5
        pennies = leftover_pennies % 5
    print(
        f'I can give you {dollars} dollars, {quarters} quarters,\n{dimes} dimes, {nickles} nickles, and {pennies} pennies.')


make_change()
