
dollar_amount = int(input('How much money do you have (in decimal format)? '))

total_pennies = round(dollar_amount) // 100 + float(dollar_amount) // 1

print(total_pennies)
