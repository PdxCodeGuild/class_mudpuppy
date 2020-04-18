#Lab 25, version 1, April 17th, 2020

class Atm:
    def __init__(account, balance = 0):
        account.negative = False
        account.balance = balance
        account.interest_rate = .01
        account.transactions = []

    def check_balance(account):     #returns the account balance
        print(f"Your account currently has ${account.balance}")
        return account.balance

    def deposit(account, amount):    #deposits the given amount in the account
        account.balance += amount
        account.transactions.append(f"User has deposited ${amount}, for a new balance of ${account.balance}")
        return account.balance

    def check_withdrawal(account, amount): 
        if (account.balance - amount) >= 0:
            print("You're good.")
            return False
        elif (account.balance - amount) < 0:
            print("Careful, your withdrawal will put in in the red.")
            return True
    
    def withdraw(account, amount):
        account.balance -= amount
        account.transactions.append(f"User has withdrawn ${amount}, for a new balance of ${account.balance}")
        return account.balance
    
    def calc_interest(account):
        interest_calc = account.balance * account.interest_rate
        print(f"Your account has earned ${interest_calc} in interest.")
        return interest_calc
    
    def print_transactions(account):
        for item in account.transactions:
            print(item, sep='\n')
        return account.transactions
        

Brea = Atm()
Brea.deposit(100)
Brea.withdraw(6)
Brea.deposit(10000)
Brea.print_transactions()