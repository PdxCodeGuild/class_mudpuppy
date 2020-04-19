"""
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
"""
# import decimal
# print("Enter number of feet ")
# number_feet = float(input(''))
# meters = 0.3048
# print(f" that equals {number_feet * meters} meters ")

"""
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
"""
import math
distance = int(input("Choose a distance: "))
user = input("Choose a unit: ")
unit_dict = { 'feet' : 0.3048, 'miles': 1609.3, 'meter': 1, 'kilometer': 1000 }
user_int = unit_dict[user]
conversion = user_int * distance
print(f"(The conversion is {conversion} ")

"""
Add support for yards, and inches.
"""

# import math
# distance = int(input("Choose a distance: ")
# user = input("Choose a unit: ")
# unit_dict = { 'feet' : 0.3048, 'miles': 1609.3, 'meter': 1, 'kilometer': 1000, 'yard' : 0.9144, 'inch' : 0.254 }
# user_int = unit_dict[user]
# conversion = user_int * distance
# print(f"(The conversion is {conversion} ")

