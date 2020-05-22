#lab25-atm.py
     
class ATM:
    def __init__(self, balance=0, interest_rate=.01):
        self.balance = balance
        self.interest_rate = interest_rate

        self.transactions = []

    def check_balance(self): 
        '''returns the account balance'''
        print(f"Your balance is {self.balance}")
        return self.balance

    def deposit(self, amount):
        '''deposits the given amount in the account'''
        print(f"Your deposit is {amount}")
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')
        print(f"Your balance is {self.balance}")

    def check_withdrawal(self, amount):
        '''returns true if the withdrawn amount won't put the account in the negative'''
        if self.balance >= amount:
            return True
        else: 
            return False
       
    def withdrawl(self, amount):
        '''withdraw(amount) withdraws the amount from the account and returns it'''
        if self.balance >= amount:
            self.balance -= amount
            print(f"Your balance is {self.balance}")
            self.transactions.append(f'User withdrew ${amount}')
        else:
            print("You do not have enough money")

    def print_transactions(self):
        print(f"Here is your list of transactions {self.transactions}")
        '''printing out the list of transactions'''
    
    def calc_interest(self):
        '''returns the amount of interest calculated on the account'''
        interest = self.balance * self.interest_rate
        print(f"Your balance is {interest}")

my_atm = ATM(balance=100)
while True:
    user_choice = input('Choose (d)eposit, (w)ithdrawl, (cb)alance, (h)istory, (q)uit: ')
    if 'd' == user_choice:
        amount = input(f'How much would you like to deposit?')
        my_atm.deposit(int(amount))
    if 'w' == user_choice:
        amount = input(f'How much would you like to withdrawl?')
        my_atm.withdrawl(int(amount))
    if 'cb' == user_choice:
        my_atm.check_balance()
    if 'h' == user_choice:
        my_atm.print_transactions()
    elif 'q' == user_choice:
        break
print(f'Thank you, please come again!')
