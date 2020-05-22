class ATM:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
        self.transactions =[]
        # self.check_withdrawl = True
    # def __repr__(self):
    #     return f"balance:{self.balance}"

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

while True:
    user_input = input("(D)eposit, (W)ithdrawl, (C)heck_balance, (H)istory? (Q)uit ")
    if user_input == "D":
        user_deposit =  int(input("How much would you like to deposit?: "))
        my_atm.deposit_amount(user_deposit)
    # print(user_deposit + my_atm.balance)
    if user_input == "W":
        user_withdrawl = int(input("How much would you like to withdraw? "))
        my_atm.withdrawl_amount(user_withdrawl)
    # print(user_withdrawl - my_atm.balance)
    if user_input == "C":
        print(my_atm.balance)
    # print(user_balance)
    if user_input == "H":
        my_atm.transactions
        my_atm.print_transaction()
    # print(user_history)
    if user_input == "Q":
        break