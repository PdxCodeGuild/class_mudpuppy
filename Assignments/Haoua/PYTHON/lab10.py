

list1 = []
i = 0


while True:
    num1 = (input("Input your first number: ")).lower()
    # print(num1.isdigit())
    if num1.isdigit():
        num2 = int(num1)
        list1.append(num2)
        
    elif num1 == "done":
        total = (sum(list1)//len(list1))
        print(f"Your average is:  {total}")
        break

    