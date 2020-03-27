#simple calculator lab v2 3.25.20

while True:
    op_input = input("What operation would you like to perform? (+, -, *, /) : ")

    if op_input == 'done':
        print("Thanks, goodbye!")
        break

    num1 = input("What is the first number? : ")

    num2 = input("What is the second number? : ")

    if op_input == "+" :
        add_sum = float(num1) + float(num2)
        print(f"{num1} + {num2}  =  {add_sum}")
        
    if op_input == "-" :
        sub_sum = float(num1) - float(num2)
        print(f"{num1} - {num2}  =  {sub_sum}")

    if op_input == "*" :
        prod = float(num1) * float(num2)
        print(f"{num1} * {num2}  =  {prod}")

    if op_input == "/" :
        div = float(num1) / float(num2)
        print(f"{num1} / {num2}  =  {div}")
    

    