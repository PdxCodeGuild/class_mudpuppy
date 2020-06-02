import random

lottery_n =[]


for i in range (0,6):
    number = random.randint(1, 99)

    while number in lottery_n:
        number = random.randint(1, 99)
    lottery_n.append(number)


lottery_n.sort()

user_n = []

for i in range(0,6):
    number_user = int(input("Pick a number between 1-99: "))
   
    user_n.append(number_user)
    user_n.sort()

print(">>>> The lotery numbers today are: ")
print(lottery_n)
print(">>>>  You chose: ")
print(user_n)

counter = 0
# for number_user in lottery_n:
if number_user in lottery_n:
    counter += 1    
print("You guessed "+ str(counter) + " number(s) accurately.")


balance = 0
ticket = 2
if counter < 1:
    balance = - ticket
    print("Unfortunately, you're out $2.00")
elif counter == 1:
    balance = 7 - ticket
    print("Yay, you win $5.00!")
elif counter == 2:
    balance = 100 - ticket
    print("You've won $98.00!")
elif counter == 3:
    balance = 50,000 - ticket
    print("Hooooray! You win $49,998.00")
elif counter == 4:
    balance = 1,000,000 - ticket
    print("Congratulations! You win $999,998.00")
elif counter == 5:
    balance = 25,000,000 - ticket
    print("WOW! You win $24,999,998.00")
else:
    print("please retry")

print("Your account balance is now: " +"$"+ "{:.2f}".format(balance))