class ATM:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
        # self.check_withdrawl = True

    def deposit_amount(self, deposit):
        self.balance += deposit

    def withdrawl_amount(self, withdrawl  ):
        self.balance -= withdrawl
    
    def check_withdrawl(self):
        if self.balance < 0:
            print("overdraft")

my_atm = ATM(1200, .1)
my_atm.deposit_amount(1200)
ATM.deposit_amount(my_atm, 1200)
print(my_atm.balance)
# my_str = 'ABC'
# print(my_str.lower())
# print(str.lower(my_str))