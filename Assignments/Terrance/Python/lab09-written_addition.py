#lab09-written_addition.py

units = {
    "m": 1,
    "ft": 0.3048,
    "mi": 1609.34,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}

user_unit = input("What unit are you using?")
user_number = input("Enter the number of units.")

user_number = int(user_number)

if user_unit == "m":
    solution = units["m"] * user_number
    print(solution)
elif user_unit == "ft":
    solution = units["ft"] * user_number
    print(solution)
elif user_unit == "mi":
    solution = units["mi"] * user_number
    print(solution)
elif user_unit == "km":
    solution = units["km"] * user_number
    print(solution)
elif user_unit == "yd":
    solution = units["yd"] * user_number
    print(solution)
else:
    solution = units["in"] * user_number
    print(solution)

# m = input("1: ")
# ft = input("Spell out a number with letters: ")
# number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# num1_int = number_dict[num1]
# num2_int = number_dict[num2]
# number_sum = num1_int + num2_int 
# print(f"The sum is {number_sum}")

# user_ft = int(input("How many feet do you want to turn into meters? "))

# m = 0.3048

# solution = m * user_ft
# print(f"the distance in meters is: {solution}")