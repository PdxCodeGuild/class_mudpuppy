#version 1
# user_ft = input("How many feet do you want to turn into meters?")
#
# user_ft = int(user_ft)
# m = 0.3048
#
# solution = m * user_ft
#
# rounded_num = round(solution, 2)
# print(solution)
# print(rounded_num)
#version 2
# units = {
#     "m": 1,
#     "ft": 0.3048,
#     "mi": 1609.34,
#     "km": 1000,
# }
#
# user_unit = input("What unit are you using?")
# user_number = input("Enter the number of units.")
#
# user_number = int(user_number)
#
# if user_unit == "m":
#     solution = units["m"] * user_number
#     print(solution)
# elif user_unit == "ft":
#     solution = units["ft"] * user_number
#     print(solution)
# elif user_unit == "mi":
#     solution = units["mi"] * user_number
#     print(solution)
# else:
#     solution = units["km"] * user_number
#     print(solution)
#Version 3
units = {
    "m": 1,
    "ft": 0.3048,
    "mi": 1609.34,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254,
}
user_unit = input("What unit are you using?: ")
user_unit2 = input("What unit do you want to convert to?: ")
user_number = int(input("Enter the number of units: "))

# user_number = int(user_number)
# if user_unit == "m":
#     solution = units["m"] * user_number
#     print(solution)
# elif user_unit == "ft":
#     solution = units["ft"] * user_number
#     print(solution)
# elif user_unit == "mi":
#     solution = units["mi"] * user_number
#     print(solution)
# elif user_unit == "km":
#     solution = units["km"] * user_number
#     print(solution)
# elif user_unit == "yd":
#     solution = units["yd"] * user_number
#     print(solution)
# else:
#     solution = units["in"] * user_number
#     print(solution)

result = (user_number * ((units[user_unit])/units[user_unit2]))
print(result)