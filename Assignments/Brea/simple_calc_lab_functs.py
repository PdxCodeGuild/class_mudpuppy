#Simple calculator lab, function version 3.25.20

ops_dict = {'+': add, '-': sub, '*': mul, '/': div}

while True:
    op_input = input("What operation would you like to perform? (+, -, *, /) : ")

    if op_input == 'done':
        print("Thanks, goodbye!")
        break

    num1 = input("What is the first number? : ")

    num2 = input("What is the second number? : ")

    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def mul(num1, num2):
        return num1 * num2

    def div(num1, num2):
        return num1 / num2

    def solution(ops_dict[op_input],(num1, num2)):
        return solution

    def arith(num1, num2, op_input):
        return (print(f"{num1} {op_input} {num2} = {solution}"))