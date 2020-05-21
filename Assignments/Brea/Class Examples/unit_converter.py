 #unit_converter.py

unit_dict = {'feet': .03048}

user_input = input("Number of feet to convert?: ")

calc = int(user_input) * unit_dict['feet']

print(f"{user_input} feet is {calc}")