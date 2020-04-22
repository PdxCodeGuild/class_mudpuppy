currency = {'dollar': 100, 'quarter': 25, 'dime': 10, 'nickle': 5, 'penny': 1}

class ATM:
    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def welcome(self):
        print('Welcome to the change machine.\n')
        self.balance = float(input('How much money do you have? (ex. 1.75) $'))

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdraw: {amount}")

    def view_transactions(self):
        print("-----Transaction History-----")
        print("\n".join(self.transactions))

    def calc_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance

    def empty_account(self):
        self.balance = round(self.balance * 100)
        if self.balance == 0:
            print('\nSorry, you have no money.')
        else:
            dollars = self.balance // currency['dollar']
            leftover_coins = self.balance % currency['dollar']
            quarters = leftover_coins // currency['quarter']
            leftover_coins = leftover_coins % currency['quarter']
            dimes = leftover_coins // currency['dime']
            leftover_coins = leftover_coins % currency['dime']
            nickles = leftover_coins // currency['nickle']
            pennies = leftover_coins % currency['nickle']
        print(
            f'\nI can give you {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies.')
        print('\nThank you! Bye!')

atm = ATM()

while True:
    print("\n\
-------------------MENU-------------------\n\
[1] Deposit      [2] Withdraw  [3] Balance\n\
[4] Transactions [5] Interest  [6] Empty Acct\n\
[0] Exit")
    try:
        command = int(input('Choose an option: '))
        if command > 6:
            print("Not a vaild option, enter 0-5.")
        elif command == 0:
            print('Thank\'s for using the ATM.')
            break
        elif command == 1:
            print("How much would you like to deposit? ")
            amount = float(input(': '))
            atm.deposit(amount)
        elif command == 2:
            print("How much would you like to withdraw? ")
            amount = float(input(': '))
            atm.withdraw(amount)
        elif command == 3:
            print(f'Your account balance is ${atm.check_balance()}')
        elif command == 4:
            atm.view_transactions()
        elif command == 5:
            atm.calc_interest()
        elif command == 6:
            atm.empty_account()
    except ValueError:
        print("Not a valid entry. Try again. ")
    except KeyboardInterrupt:
        print("\nYou quit, thank's for using the atm.")
        break
