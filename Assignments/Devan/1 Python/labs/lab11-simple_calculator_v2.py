'''
Lab 11: Simple Calculator

Version 2

Allow the user to keep performing operations until they say 'done'. Use while True and break
'''

def calc_2_nums(usr_operator, num1, num2):
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
    else:
        print('That\'s not a valid input. Try again. ')
    return

while True:
    usr_operator = input('What is the operation you would like to perform, or type done:  ')
    if usr_operator == 'done':
        break
    num1 = (input('What is the first number? '))
    num2 = (input('What is the second number? '))
    num1 = float(num1)
    num2 = float(num2)
    calc_2_nums(usr_operator, num1, num2)
