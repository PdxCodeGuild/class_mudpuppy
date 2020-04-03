op = input("What operation would you like to perform?: ") #Choosing what type of calcualtion to perform

num1 = input("What is the first number?: ") #user picking first number
num2 = input("What is the second number?: ") #user picking second number

if op == "+": #this is telling python if op is the addition symbol then do what it is after the semi colon this if statement runs the addition 
    add = float(num1) + float(num2) # this part of the code is wrapping the users first num so that python can use it with out converting it back to a int. it is a variable to use in the print function next
    print(f"{num1} plus {num2} equals {add}")

if op == "-":# this one for subtraction
    sub = float(num1) - float(num2)
    print(f"{num1} minus {num2} equals {sub}")

if op == "*":# multiplication 
    mult = float(num1) * float(num2)
    print(f"{num1} times {num2} equals {mult}")

if op == "/":# divsion
    div = float(num1) / float(num2)
    print(f"{num1} divided by {num2} equals {div}")