# # from random import randint
# # grade = int(input("Enter a number representing your letter grade (0-100): "))
# # def check_grade(grade):
# #     if grade is >== 95:
# #         return "A"
# #     print("A") 
# #     elif grade >== 90:
# #         return 
# #     print("A")
# #     elif grade >== 85:
# #         return 
# #     print("B")
# #     elif grade >== 80:
# #         return 
# #     print("C")
# #     elif grade >== 70:
# #         return 
# #     print("C")
# #     elif grade >== 65:
# #         return 
# #     print("D")
# #     elif grade >== 60:
# #         return 
# #     print("D")
# #     elif grade >== 55: 
# #         return 
# #     print("F")
# #     else:
# #         return 
# #     print("Did you even come to class?")
# import random
# # from random import randint
# # import grades
# # from grades import check_grades as cg #(replace check_grades with cg) #if we want to import only the function. remove grade.
# grade = int(input("Enter your grade(0-100):"))
# # rival - random.randint(0,100)
# # # x = int(grade)
# AAA = 96, 97, 98, 99, 100, 101
# AA = 95
# A = 90, 91, 92, 93, 94
# BBB = 86, 87, 88, 89
# BB = 85
# B = 80, 81, 82, 83, 84
# CCC = 76, 77, 78, 79
# CC = 75
# C = 70, 71, 72, 73, 74
# DDD = 66, 67, 68,  69
# DD = 65
# D = 60, 61, 62, 63, 64
# F = 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
# W = 0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49
# # def letter_grade(grade):
# #     # while True:
#         for grade in AAA:
#             if grade == AAA:
#                 AAA.append(grade)
#                 break
#                 return "A+"
#             elif grade == AA:
#                 return "A"
#             elif grade == A:
#                 return "A-"
#             elif grade == BBB:
#                 return "B+"
#             elif grade == BB:
#                 return "B"
#             elif grade == B:
#                 return "B-"
#             elif grade == CCC:
#                 return "C+"
#             elif grade == CC:
#                 return "C")
#             elif grade == C:
#                 print("C-")
#             elif grade == DDD:
#                 print("D+")
#             elif grade == DD:
#                 print("D")
#             elif grade == D:
#                 print("D-")
#             elif grade == F:
#                 print("F")
#             elif grade == W:
#                 print("Did you even attend class?")
# letter_grade(grade)
# # print(letter_grade(grade))







'''
# list1 = grade.append[]
def letter_grade(grade):
        if grade >= A+:
            return "A+"
        # print("A+")
        elif grade == 95:
            return "A"
        elif grade <= 95:
            return "A-"
        elif grade >= 85:
            return "B+"
        elif grade == 85:
            return "B-"
        elif grade <= 80:
            return "B"
        elif grade >= 75:
            return "C+"
        elif grade == 70:
            return "C"
        elif grade <= 70:
            return "C-"
        elif grade >= 65:
            return "D+"
        elif grade == 65:
            return "D"
        elif grade <= 60:
            return "D-"
        elif grade >= 55:
            return "F+"
        elif grade == 50:
            return "F"
        else:
            return "Did you even attend class bro?"

# check_grade()
print(check_grade(grade))

# user_grade = grades.check_grades(user)
# rival_grade = grades.check_grades(rival)

# print(f"The user got a {user}{user_grade} and your rival got a {rival}{rival_grade}")
'''



grade = int(input("Please enter your grade in numerical form (0-100) : "))

def my_function(grade):
    # while user = "Yes", "Y", "y", "yes"
    if grade > 95:
        return "A+"
    elif grade == 95:
        return "A"
    elif grade > 90:
        return "A-"
    # elif grade > 90:
    #     print("A-")
    elif grade > 85:
        return "B+"
    elif grade == 85:
        return "B"
    elif grade > 80:
        return "B-"
    elif grade > 75:
        return "C+"
    elif grade == 75:
        return "C"
    elif grade > 70:
        return "C-"
    elif grade > 65:
        return "D+"
    elif grade == 65:
        return "D"
    elif grade > 60:
        return "D-"
    elif grade < 60:
        return "Did you even come to class bro?"
print(my_function(grade))
response = ["Yes", "Y", "y", "yes"]
user = input("Would you like to enter a second grade? Y/N :")
user2 = user.lower()
while True:
    if user2 in response:
        grade2 = int(input(f"Please enter your grade 0-100 : "))
    # i += i+ 0
        print(my_function(grade2))
        user = input("Would you like to enter a second grade? Y/N :")
        user2 = user.lower()
        continue
    else:
        print("Thank you for playing!")
        break

# response = ["Yes", "Y", "y", "yes"]
# while user = response:
#     if user = "Y", "Yes":
#         print(my_function(grade))
