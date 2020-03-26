def get_function(op):
    return operators[op]

def add(x,y):
    return x + y

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def eval(fn, n1, n2):
    return fn(n1, n2)

operators = {'+': add, '-': minus, '*': multiply}

operator = input('enter your operator: ')
n1 = int(input('enter the first number: '))
n2 = int(input('enter the second number: '))

print(eval(get_function(operator), n1, n2))