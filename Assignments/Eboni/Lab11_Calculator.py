while True:
    operation = input ("Enter your operation (+, -, *, /): ")
    first_num = float(input("Enter your first number: "))
    second_num = float(input("Enter your second number: "))

    if operation == "+":
        answer = first_num + second_num
        print(f"{first_num} + {second_num} = {answer} ")
    elif operation == "-":
        answer = first_num - second_num
        print(f"{first_num} + {second_num} = {answer} ")
    elif operation == "*":
        answer = first_num * second_num
        print(f"{first_num} * {second_num} = {answer} ")
    elif operation == "/":
        answer = first_num / second_num
        print(f"{first_num} / {second_num} = {answer} ")
    user_input = input("Please type stop to stop: ")
    if user_input == 'stop':
        break