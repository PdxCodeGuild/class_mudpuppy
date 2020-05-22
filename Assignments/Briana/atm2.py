class ATM():
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
        self.transactions = []


    def check_balance(self):
        return self.balance


    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'User withdrew {amount}')
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited {amount}')
        return self.balance

    def calc_interest(self):
        x =  int(self.balance)*self.interest 
        return x

    def print_transactions(self):
        return self.transactions



bris_account = ATM(100, .04)

while True:
    user_input = input('what would you like to do (deposit, withdraw, check balance, history, calculate interest)? ')
    if user_input == 'deposit':
        amount = input('How much would you like to deposit? \n$ ')
        print(bris_account.deposit(int(amount)))
        # print(bris_account.check_balance())
        print(bris_account.print_transactions())

    if user_input == 'withdraw': 
        amount = input('How much would you like to withdraw? \n$ ')
        print(bris_account.withdraw(int(amount)))
        print(bris_account.check_balance())
        print(bris_account.print_transactions())

    if user_input == 'check balance': 
        print(bris_account.check_balance())

    if user_input == 'history': 
        print(bris_account.print_transactions())

    if user_input == 'cal': 
        print(bris_account.calc_interest())

    if user_input == 'quit':
        break 




