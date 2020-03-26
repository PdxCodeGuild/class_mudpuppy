#Simple calculator lab, function version 3.25.20

while True:
    input()
    op_input = input("What operation would you like to perform? (+, -, *, /) : ")

    if op_input == 'done':
        print("Thanks, goodbye!")
        break

    num1 = int(input("What is the first number? : "))

    num2 = int(input("What is the second number? : "))

    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def mul(num1, num2):
        return num1 * num2

    def div(num1, num2):
        return num1 / num2
    
    ops_dict = {'+': add, '-': sub, '*': mul, '/': div}

    def solution(fn, num1, num2):
        return fn(num1, num2)
        
    (print(f"{num1} {op_input} {num2} = {solution(ops_dict[op_input], num1, num2)}"))