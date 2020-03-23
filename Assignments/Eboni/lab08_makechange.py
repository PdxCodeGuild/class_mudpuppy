"""
Let the user enter how many pennies they have, and convert their pennies into larger coins and leftover pennies. Version 1
Convert the user's pennies into the maximum number of quarters. For example, if the user enters 136, break that 136 into quarters (5) and pennies (11).
"""


# print("How many pennies do you have? ")
# pennies = int(input(''))
# print(f"That means you have {pennies//25} quarters and {pennies % 25} pennies lefotver. ")

"""
Convert the user's pennies into the maximum number of quarters, then the maximum number of dimes, then the maximum number of nickels. Have the user enter the total number in pennies. For example, break 136 into quarters (5), dimes (1), nickles (0) and pennies (1).
"""

# print("How many pennies do you have to start? ")
# pennies = int(input(''))
# print ("I'll convert quarters, nickles and dimes ")
# quarters = ['5']
# dimes = ['1']
# nickels = ['0']
# pennies_leftover = ['1']
# print(f"That means you have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies_leftover} pennies. ")

"""
Have the user enter a dollar amount (1.36), convert this to the total in pennies, and proceed as before. Do this with float() and round().
"""
# import decimal
# print("Enter a dollar amount. ")
# dollars = float(input('$'))
# print(dollars)
# pennies = int(dollars) * 136
# print(pennies)


"""
In a while loop, let the user add or subtract a dollar amount to the current coin value, and then convert the resulting value into the smallest number of coins possible.

"""
quarters = ['5']
dimes = ['1']
nickels = ['0']
pennies_leftover = ['1']
print(int(f"you have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies_leftover} pennies"))










