import random

penny = 1
nickle = 5
dime = 10
quarter = 25
dollar = 100
num_of_pennies = int(input('How many pennies do you have? '))
print(f'I can give you {num_of_pennies // 25} quarters and {num_of_pennies % 25} pennies.')
