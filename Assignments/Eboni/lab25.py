class ATM:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
        self.transactions =[]
        # self.check_withdrawl = True

    def deposit_amount(self, deposit):
        self.balance += deposit
        self.transactions.append(f"You deposited {deposit}")
        # this needs to be copied in a few places

    def check_withdrawl(self, withdrawl):
        
        if self.balance >= withdrawl:
            print("You can withdraw ")
            return True
        else:
            return False

    def withdrawl_amount(self, withdrawl):
        if self.check_withdrawl(withdrawl):
            self.balance -= withdrawl
        self.transactions.append(f"You withdrew {withdrawl}")
   

    def calc_interest(self):
        self.balance += 0.1

    def print_transaction(self):
        print(self.transactions)

my_atm = ATM(1200, .1)
my_atm.withdrawl_amount(1200)
ATM.deposit_amount(my_atm, 1200)
print(my_atm.balance)
my_atm.print_transaction()