
class ATM:
    def __init__(self, balance=0, interest_rate=.01):
        self.balance = balance
        self.interest_rate = interest_rate

       

    def check_balance(self): 
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        
    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        else:
            return True    

       
    def withdrawl(self, amount):
        self.balance -= amount

    
    def calc_interest(self):
        interest = self.balance * self.interest_rate
       
