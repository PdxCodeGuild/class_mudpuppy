#lab08-makechange.py

# Let the user enter how many pennies they have, and convert their pennies into larger coins and leftover pennies.
# Version 1

# Convert the user's pennies into the maximum number of quarters. For example, if the user enters 136, break that 136 into quarters (5) and pennies (11).

print("I have a change converter. How many pennies do you have? ")
change_amount = int(input(': '))
# print(f"That would equal {change_amount // 25} quarters and you would have {change_amount % 25} pennies leftover.")
print(f"That would equal {change_amount // 25} quarters.") 

leftover_pennies = change_amount % 25

# change_amount = int(input(': '))
print(f"And, {leftover_pennies // 10} dimes leftover.") #{change_amount % 10} pennies leftover.")

change_amount = int(input(': '))
print(f"And, {change_amount // 5} nickels leftover.") #{change_amount % 5} pennies leftover.")

