#  Lab 11: Simple Calculator Version 3

def get_operator(op):
    return operators[op]

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def eval(fn, n1, n2):
    return fn(n1, n2)

operators = {'+': add, '-': subtract, '*': multiply, '/': divide}

while True:
    try:
        operator = input('Enter your operator (+, -, *, /) or done: ')
        if operator == 'done':
            print('\nThanks for using the calculator.')
            break
        if operator not in operators:
            print('Not a vaild operator...')
        else:
            n1 = int(input('Enter the first number: '))
            n2 = int(input('Enter the second number: '))
            print(eval(get_operator(operator), n1, n2))
    except KeyboardInterrupt:
        print('\nThank You')
        break
