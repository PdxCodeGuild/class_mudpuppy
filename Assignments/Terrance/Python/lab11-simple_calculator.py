#lab11-simple_calculator.py

# Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and ea*ch operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

# > What is the operation you'd like to perform? +
# > What is the first number? 5
# > What is the second number? 12
# > 5 + 12 = 17

user_input = input("Which operation would you like to use? ")
user_1number = int(input("What is your first number? "))
user_2number = int(input("What is your second number? "))

if user_input == "*":
    print(user_1number * user_2number)

elif user_input == "/":
    print (user_1number / user_2number)

elif user_input == "-":
    print (user_1number - user_2number)

elif user_input == "+":
    print (user_1number + user_2number)




# while True:
#     # paste code here
#     var1 = input("Please type cat >")
#     container.append(var1)
#     if var1 == 'cat':
#         break

# container.remove("cat")
# print(container)

