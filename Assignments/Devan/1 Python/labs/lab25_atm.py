import platform


MENU_OPTIONS = {0: "Exit",
                1: "Deposit",
                2: "Withdraw",
                3: "Balance",
                4: "Transactions",
                5: "Interest",
                6: "Empty Account"
                }


class ATM:
    def __init__(self, balance=0, interestRate=0.001):
        self.balance = balance
        self.interestRate = interestRate
        self.transactions = []
        self.transactionID = 1

    def welcome(self):
        clearScrn()
        print('\nWelcome to the ATM.\n\nHow much money do you have? (ex. 1.75) ')
        try:
            self.balance = float(input('$ '))
            self.transactions.append(
                f"ID:{self.transactionID}     Start Balance: {self.balance}")
            self.transactionID += 1
        except:
            print("\nPlease enter a valid number.")
            self.welcome()
        clearScrn()
        self.checkBalance()

    def mainMenu(self):
        while True:
            print(f'\n{"-"*13}MENU{"-"*13}\n')
            for pair in MENU_OPTIONS.items():
                print(": ".join(str(i) for i in pair))
            try:
                command = int(input('\nChoose an option: '))
                if command >= len(MENU_OPTIONS):
                    clearScrn()
                    print(
                        f"\nNot a vaild option, enter 0 - {len(MENU_OPTIONS)-1}.")
                elif command == 0:
                    print('\nThank\'s for using the ATM.')
                    break
                elif command == 1:
                    print("\nHow much would you like to deposit? ")
                    amount = float(input('$ '))
                    self.deposit(amount)
                    self.checkBalance()
                elif command == 2:
                    print("\nHow much would you like to withdraw? ")
                    amount = float(input('$ '))
                    self.withdraw(amount)
                    self.checkBalance()
                elif command == 3:
                    self.checkBalance()
                elif command == 4:
                    self.viewTransactions()
                elif command == 5:
                    self.calcInterest()
                elif command == 6:
                    self.emptyAccount()
                    break
            except ValueError:
                print("\nNot a valid entry. Try again. ")
            except KeyboardInterrupt:
                print("\nYou quit, thank's for using the ATM.")
                break

    def checkBalance(self):
        clearScrn()
        print(
            f'\nYour account balance is $ {"{:,.2f}".format(self.balance)}')
        return self.balance

    def deposit(self, amount):
        clearScrn()
        self.balance += amount
        self.transactions.append(
            f"ID:{self.transactionID}     Deposit: {amount}")
        self.transactionID += 1

    def withdraw(self, amount):
        clearScrn()
        self.balance -= amount
        self.transactions.append(
            f"ID:{self.transactionID}     Withdraw: {amount}")
        self.transactionID += 1

    def viewTransactions(self):
        clearScrn()
        print("\n-----Transaction History-----\n")
        print("\n".join(self.transactions))

    def calcInterest(self):
        self.balance += self.balance * self.interestRate
        self.checkBalance()
        print(
            f"Your daily interest is {'{: .2f}'.format(self.balance * self.interestRate)}")
        return self.balance

    # def makeChange(self):
    #     total = self.balance
    #     CURRENCY = {'hundred': 10000,
    #                 'fifty': 5000,
    #                 'twenty': 2000,
    #                 'ten': 1000,
    #                 'five': 500,
    #                 'dollar': 100,
    #                 'quarter': 25,
    #                 'dime': 10,
    #                 'nickle': 5,
    #                 'penny': 1}

    #     print('I can give you', end=' ')
    #     for currency in CURRENCY.items():
    #         if (total // currency[1]) != 0:
    #             print((total // currency[1]), str(currency[0]), end=', ')
    #             total = total % currency[1]

    def emptyAccount(self):
        CURRENCY = {'hundred': 10000,
                    'fifty': 5000,
                    'twenty': 2000,
                    'ten': 1000,
                    'five': 500,
                    'dollar': 100,
                    'quarter': 25,
                    'dime': 10,
                    'nickle': 5,
                    'penny': 1}
        clearScrn()
        self.balance = round(self.balance * 100)
        if self.balance == 0:
            print('\nSorry, you have no money.')
        else:
            # self.makeChange()
            hundreds = self.balance // CURRENCY['hundred']
            leftoverDollars = self.balance % CURRENCY['hundred']
            fiftys = leftoverDollars // CURRENCY['fifty']
            leftoverDollars = leftoverDollars % CURRENCY['fifty']
            twentys = leftoverDollars // CURRENCY['twenty']
            leftoverDollars = leftoverDollars % CURRENCY['twenty']
            tens = leftoverDollars // CURRENCY['ten']
            leftoverDollars = leftoverDollars % CURRENCY['ten']
            fives = leftoverDollars // CURRENCY['five']
            leftoverDollars = leftoverDollars % CURRENCY['five']
            ones = leftoverDollars // CURRENCY['dollar']
            leftoverDollars = leftoverDollars % CURRENCY['dollar']
            leftoverCoins = leftoverDollars % CURRENCY['dollar']
            quarters = leftoverCoins // CURRENCY['quarter']
            leftoverCoins = leftoverCoins % CURRENCY['quarter']
            dimes = leftoverCoins // CURRENCY['dime']
            leftoverCoins = leftoverCoins % CURRENCY['dime']
            nickles = leftoverCoins // CURRENCY['nickle']
            pennies = leftoverCoins % CURRENCY['nickle']
            print(
                f'\nI can give you {hundreds} hundreds, {fiftys} fiftys, {twentys} twentys, {tens} tens, {fives} fives, {ones} ones, {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies.')
            print('\nThank you! Bye!')
        return


def clearScrn():
    systemOS = platform.system()
    if systemOS == "Windows":
        print(chr(12))
    elif systemOS == "Darwin" or "Linux":
        esc = chr(27)
        print(esc + '[2J' + esc + '[0;0H')
    else:
        return


atm = ATM()
atm.welcome()
atm.mainMenu()
