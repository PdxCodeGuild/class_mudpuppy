
amount = float(input("Enter a dollar amount (0-99) : "))
ver = amount.is_integer()
print(ver)

if ver is False:
    print(amount//.25, "quarters") 
    amount = amount%.25

    print(amount//.10, "dimes")
    amount = amount%.10

    print(amount//.05, "nickles")
    amount = amount%.05

    
    print(amount//.01, "pennies")
    amount = amount%.01

elif ver is True:
    print(amount//25, "quarters") 
    amount = amount%25
    print(amount//10, "dimes")
    amount = amount%10
    print(amount//5, "nickles")
    amount = amount%5
    print(amount//1, "pennies")
    amount = amount%1

