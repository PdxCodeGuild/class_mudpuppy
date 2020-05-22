
x = float(input('Please enter an amount between 0-99:'))
# print(x//.25, "quarters")
# x = x%25
# print(x//.10, "dimes")
# x = x%10
# print(x//.5, "nickles")
# x = x%.05
# print(x//.01, "pennies")
# x = x%.01/100

# q = .25
# d = .10
# n = .05
# p = .01

# 3.36
# 3.25
quarters = (get_user_input//.25)
# 13
# 56
quarters_remainder = (get_user_input%.25)
# 0.1099999
dimes = (quarters_remainder//.10)
# 1.0
dimes_remainder = (quarters_remainder%.10)
# 0.05999
nickels = (get_user_input//.05)

nickels_remainder = (dimes_remainder%.05)

pennies = (get_user_input//.01)

pennies_remainder =(nickels_remainder//.01)

# pennies_remainder = (nickels_remainder%.05)

result = (f'There are Q'{quarters} {dimes} {nickels} {pennies}')
print(result)
# Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136
# Have the user enter a dollar amount (1.36), convert this to the total in pennies.