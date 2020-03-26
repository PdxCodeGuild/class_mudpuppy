'''
Lab 11: Simple Calculator

Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input.
'''


usr_operator = input('What is the operation you would like to perform? ')
num1 = float(input('What is the first number? '))
num2 = float(input('What is the second number? '))

if usr_operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif usr_operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif usr_operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif usr_operator == '/':
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
