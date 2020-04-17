num1 =float(input("Enter first number: ")) #they have to insert a number otherwise we get an error
qp = input("Enter operator: ")
num2 = float(input("Enter second number: "))

def myfunc(num1, num2):
    if qp == "+":
        print(num1 + num2)
    elif qp == "-":
        print(num1 - num2)
    elif qp == "/" :
        print(num1 / num2)
    elif qp == "*":
        print(num1 * num2)
    else: 
        print("Invalid operator")
myfunc(num1, num2)

repeat = str(input("Would you like to input another equation? : ")).lower()
responses = "yes", "y", "yeah", "yah", "si"

while True:
    if repeat in responses:
        num3 = float(input("Enter first number: "))
        qp = input("Enter operator: ")
        num4 = float(input("Enter second number: "))
        myfunc(num3, num4) #putting print in front of myfunc(makes it print out none)
        responses = input("Would you like to input another equation? :").lower()
        
        # num3 = float(input("Enter first number: "))
        # qp2 = input("Enter operator: ")
        # num4 = float(input("Enter second number: "))
        # print(myfunc(num3, num4))
        # print(myfunc(num1, num2))
    
    elif repeat not in responses:
        # num3 = float(input("Enter first number: "))
        # qp = input("Enter operator: ")
        # num4 = float(input("Enter second number: "))
        # print(myfunc(num3, num4))
        # input("Would you like to input another equation? :").lower()
        print("Dueces!!")
        break

    

