#Lab 20, version 1.py, April 8th, 2020

user_input = input("Please input your credit card number: ")

def check_credit_card(inpt):
    cc_list = []
    for piece in inpt:
        piece = int(piece)
        cc_list.append(piece)
        
    check_num = cc_list[-1]
    cc_list = cc_list[:-1]
    cc_list.reverse()

    for i, num in enumerate(cc_list):
        if i % 2 == 0:
            cc_list[i] = num * 2
    
    for i, num in enumerate(cc_list):
        if num > 9:
            cc_list[i] = num - 9

    for num in cc_list:
        total = sum(cc_list)

    total_str = str(total)

    total_lst = []
    for piece in total_str:
        piece = int(piece)
        total_lst.append(piece)

    check_num2 = total_lst[1]

    check_lst = []
    check_lst.append(check_num)
    check_lst.append(check_num2)

    if check_lst[0] == check_lst[1]:
        print("Your credit card is authenticated!")

    if check_lst[0] != check_lst[1]:
        print("Sorry, we cannot authenticate your card at this time")

    return check_lst

check_credit_card(user_input)




