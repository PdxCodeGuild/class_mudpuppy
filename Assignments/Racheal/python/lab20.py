# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.****


# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!

credit_card_digits = [5,1,7,8,0,5,9,4,2,9,4,4,7,9,7,3]

# # def input():
# # x = list(int(input("Enter the card number: "))
# #     firsthalf= list()
# #     sechalf= list()
# # for i in x:
# #     x = int(input())
# #     if i<9:
# #         firsthalf.append(x)
# #     else: 
# #         sechalf.append(x)

def get_digit_dict():
    credit_card_digits = [5,1,7,8,0,5,9,4,2,9,4,4,7,9,7,3]
    check_digit = credit_card_digits.pop(15)
    digit_dict = {"credit_card_digits": credit_card_digits, "check_digit": check_digit}
    return digit_dict

def reverse_digit_list(digit_dict):
    digit_dict["credit_card_digits"].reverse()
    return digit_dict

def get_double_digits(digit_dict):
    for i in digit_dict['credit_card_digits'][::2]:
        i *= 2
    return digit_dict

def get_subtracted_digits(digit_dict):
    for i in digit_dict['credit_card_digits']:
        if i > 9:
            i -= 9
    return digit_dict

# possibly, another for loop and another function 


# def process(digit_dict): 
#     sum1=int(0)
#     sum2=int(0)
#     for i in firsthalf: 
#         sum1=sum1+i 
#     for i in sechalf: 
#         sum2=sum2+i
#     print(sum1, sum2)

#     if sum1>sum2:
#         diff=sum1-sum2
#     else:
#         diff=sum2-sum1

#     if (diff/2) != 0: 
#         print("CARD IS VALID ")
#     else:
#         print("CARD IS INVALID ")

# def checkSecondDigits(num):
#     length = len(num)
#     sum =  0
#     for i in range(length-2,-1,-2):
#       number = eval(num[i])
#       number = number * 2
#       if number > 9:
#           strNumber = str(number)
#           number = eval(strNumber[0]) + eval(strNumber[1])
#           sum += number
#       return sum

# def odd_digits(num):
#     length = len(num)
#     sumOdd = 0
#     for i in range(length-1,-1,-2):
#         num += eval(num[i])
#     return sumOdd

# def c_length(num):
#     length = len(num)
#     if num >= 13 and num <= 16:
#         if num [0] == "4" or num [0] == "5" or num [0] == "6" or (num [0] == "3" and num [1] == "7"):
#              return True
#     else:
#         return False

# def main():
#     filename = input("What is the name of your input file? ")
#     infile= open(filename,"r")
#     # initialize num here
#     num = cc = (infile.readline().strip())
#     print(format("Card Number", "20s"), ("Valid / Invalid"))
#     print("------------------------------------")
#     while cc!= "EXIT":
#         even = checkSecondDigits(num)
#         odd = odd_digits(num)
#         c_len = c_length(num)
#         tot = even + odd

#         if c_len == True and tot % 10 == 0:
#             print(format(cc, "20s"), format("Valid", "20s"))
#         else:
#             print(format(cc, "20s"), format("Invalid", "20s"))
#         num = cc = (infile.readline().strip())