#Lab 25, version 3, April 17th, 2020

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

 if __name__ == "__main__":       
    Brea = Atm()

    while True:
        user_input1 = input("Would you like to deposit, withdraw, check balance, check history, or quit? : ")

        if user_input1 == 'deposit':
            user_input2 = int(input("How much would you like to deposit? : "))
            Brea.deposit(user_input2)

        elif user_input1 == 'withdraw':
            user_input3 = int(input("How much would you like to withdraw? : "))
            if Brea.balance - user_input3 <= 0:
                user_input4 = input("This will drain your account. Are you sure? : ")
                if user_input4 == 'no':
                    break
                elif user_input4 == 'yes':
                    Brea.withdraw(user_input3)

        elif user_input1 == 'check balance':
            Brea.check_balance()
        
        elif user_input1 == 'check history':
            Brea.print_transactions()
        
        elif user_input1 == 'quit':
            print("Thank you for banking with the Piggy Bank!")
            break
        
        else:
            print("Sorry, I don't understand.")