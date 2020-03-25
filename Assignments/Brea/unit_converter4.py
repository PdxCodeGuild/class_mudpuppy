 #unit_converter4.py

unit_dict = {'feet': 3.2808, 'miles': .000621371, 'meters': 1, 'kilometers': .001, 'yards': 1.0936, 'inches': 39.3701}

user_input1 = input("What is the distance? : ")
user_input2 = input("What are the input units? : ")
user_input3 = input("What are the output units? : ")

calc = int(user_input1) / unit_dict[user_input2] * unit_dict[user_input3]

print(f"{user_input1} {user_input2} is {calc} {user_input3}") #add output unit to this line