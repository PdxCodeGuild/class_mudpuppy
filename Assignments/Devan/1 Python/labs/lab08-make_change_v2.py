num_of_pennies = int(input('How many pennies do you have? '))
if num_of_pennies < 0:
    print('You must enter a postitive number')
else:
    quarters = num_of_pennies // 25
    dimes = (num_of_pennies % 25) // 10
    nickles = num_of_pennies % 25 % 10 // 5
    pennies = num_of_pennies % 5
print(
    f'I can give you {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies.')
