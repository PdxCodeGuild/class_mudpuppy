#lab11-simple_calculator.py

user_input = input("Which operation would you like to use? ")
user_1number = int(input("What is your first number? "))
user_2number = int(input("What is your second number? "))

if user_input == "*":
    print(user_1number * user_2number)

elif user_input == "/":
    print(user_1number / user_2number)

elif user_input == "+":
    print(user_1number + user_2number)

elif user_input == "-":
    print(user_1number - user_2number)