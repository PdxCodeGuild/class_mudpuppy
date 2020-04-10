# deconstruct_functions.py
VERSION = 1

if VERSION == 1:
    def add_one(in_num):
        return in_num + 1

    print(add_one(5))

elif VERSION == 2:
    def add_nums(num1, num2):
        return num1 + num2

    print(add_nums(3, 10))

elif VERSION == 3:
    def add_nums(num1, num2):
        return num1 + num2

    def add_one(in_num):
        return in_num + 1

    print(add_nums(3, add_one(3)))

elif VERSION == 4:
    def add_or_multiply(num1, num2, op):
        if op == 'add':
            return num1 + num2
        elif op == 'multiply':
            return num1 * num2

    print(add_or_multiply(3, 10, 'multiply'))

elif VERSION == 5:
    def add_and_subtract_one(num1, num2):
        return num1 + num2 - 1

    def multiply_and_negate(num1, num2):
        return num1 * num2 * -1

    print(multiply_and_negate(add_and_subtract_one(3, 2), 5))
