
'''version1 & 2'''

# n = int(input("Enter a number : "))
# def Words(n):
#  units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
#  teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
#  tens = ["Twenty","Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
#  if n <=9:
#     return units[n]
#  elif n >= 10 and n <= 19:
#     return teens[n-10]
#  elif n >= 20 and n <= 99:
#     return tens[(n//10)-2] + " " + (units[n % 10] if n % 10 !=0 else "")
#  elif n >= 100 and n <= 999:
#     return Words(n//100) + " Hundred " + (Words(n % 100) if n % 100 !=0 else "")
# print(Words(n))


'''part3'''
# num_list = [(900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
#            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

# num = int(input("Enter a number : "))
# def n_roman(num):
#     roman = ""
#     while num > 0:
#         for i, r in num_list:
#             while num >= i:
#                 roman += r
#                 num -= i
#     return roman
# print(n_roman(num))

'''part4'''
