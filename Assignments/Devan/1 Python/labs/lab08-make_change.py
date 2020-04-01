class Change_Machine:
    currency = {'dollar': 100, 'quarter': 25, 'dime': 10, 'nickle': 5, 'penny': 1}
    actions = ['deposit', 'withdraw', 'empty account', 'check balance']

    def actions(self):
        print('\nWhat would you like to do?\n')
        user_action = input('Deposit, Withdraw, Empty Account, Check Balance, or Exit. ')
        user_action = user_action.lower()
        if user_action == actions[0]:
            machine.deposit()
        if user_action == actions[1]:
            machine.withdraw()
        if user_action == actions[2]:
            machine.empty_account()
        if user_action == actions[3]:
            machine.receipt()

    def welcome(self):
        print('Welcome to the change machine.\n')
        self.balance = float(input('How much money do you have? (ex. 1.75) $'))
        machine.actions()

    def deposit(self):
        amount = float(input('\nHow much would you like to add? '))
        self.balance += amount
        round(self.balance)
        print(f'\nYou have ${self.balance} available.')
        machine.actions()

    def withdraw(self):
        amount = float(input('\nHow much would you like to withdraw? '))
        self.balance += (amount * -1)
        print(f'\nYou have ${self.balance} remaining.')
        machine.actions()

    def receipt(self):
        print(f'Your available balance is ${self.balance}')
        machine.actions()

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


machine = Change_Machine()

machine.welcome()
