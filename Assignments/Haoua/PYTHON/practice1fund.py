
'''problem 1'''
# num = int(input("enter a number : "))

# def even(num):
#     
#     if (num % 2) == 0:
#         return f"{num} is even"
#     if num % 2 != 0:
#         return f"{num} is odd"
# print(even(num))

'''problem 2'''
# i = 0
# num_list = []

# while i < 2:
#     num = int(input("Enter an integer : "))
#     num_list.append(num)
#     i += 1



# def input_b():
#     if num_list[0] < 0 and num_list[1] < 0:
#         print(False)
#         return False #why doesn't return pop up on the user end, 
#         #how do I get return to print?
#     elif num_list[0] < 0 and num_list[1] > 0:
#         print(True)
#     elif num_list[0] > 0 and num_list[1] > 0:
#         print(False)
#     elif num_list[0] > 0 and num_list[1] < 0:
#         print(True) 
    
# input_b()


'''problem 3: Write a function that returns True if a number within 10 of 100'''

# user = int(input("Enter a number: "))
# def main(user):
#     if user >= 10 and user <= 100:
#         print(True)

#     else:
#         print(False)
# main(user)

'''problem 4'''
# parameters = []

# def main():
#     i = 0
#     while i < 3:
#         user = int(input("enter a number: "))
#         parameters.append(user)
#         i += 1
#     print(max(parameters))
# main()

'''problem 5'''

print([2<< exponent for exponent in range(20)])

'''for exp in range(17):
    print(2**exp)'''