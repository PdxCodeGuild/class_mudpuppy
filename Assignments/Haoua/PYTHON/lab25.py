User_Bal = 250


class Bank_Account():
    def __init__(self, balance=0, print_transactions=[], interest=.1):
        self.balance = balance
        # self.print_transactions = print_transactions
        self.print_transactions = []
        self.interest = interest
    def ch_bal(self):
        return f"Your Current Balance : ${self.balance}.00"
    def deposit(self, amount):
        self.balance = self.balance + amount
        '''self.print_transactions''' 
        self.print_transactions.append(f'You Deposited : {amount}.00')
        # User_Bal += amount 
        return f"You deposited {amount} dollars.\n Your Current Balance is : ${self.balance}.00"
    def ch_with(self, amount):
        if amount < self.balance:
            return True + "Insufficient Funds"
            
    def withd(self, amount):
        self.balance = self.balance - amount
        '''self.print_transactions = ''' 
        self.print_transactions.append(f"You Withdrew {amount}")
        # User_Bal -= amount
        return f'You withdrew {amount}.00 dollars.\n Your New Balance is :$ {self.balance}.00'
    def get_transactions(self):
        return self.print_transactions
    def interest_r(self, interest):
        return f" Your monthly interest is: {self.balance * self.interest} : Interest Rate: .01"

def main():
    atm_1 = Bank_Account(250, [], 0.1)
    User_Bal = 250
    while True:
        user = int(input('What would you like to? 1. Deposit    2. Withdrawal   3. Balance  4. History  5. Exit'))
        
        # if 5 != user:
        if user == 1:
            user_amount = int(input("How much Shmoneyy would you like to Deposit? : "))
            # user_amt1 = "{:.2f}".format(amount)
            print(atm_1.deposit(user_amount))
        if user == 2:

            user_amount = int(input("How much Would you like to Withdrawal? : "))
            if user_amount <= User_Bal:
                User_Bal -= user_amount
            # user_amt1 = "{:.2f}".format(amount)
                print(atm_1.withd(user_amount))
            else:
                print("insuff funds")
        if user == 3:
            print(atm_1.balance)
        if user == 4:
            print(atm_1.print_transactions)
            print(f"Your Accumulated Interest : ${atm_1.interest*atm_1.balance}0")
        if user == 5:
            print('Thank you, Goodbye!')
            break
main()