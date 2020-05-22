 #unit_converter3.py

unit_dict = {'feet': .03048, 'miles': 1609.34, 'meters': 1, 'kilometers': 1000, 'yards': .9144, 'inches': .0254}

user_input1 = input("What is the distance? : ")
user_input2 = input("What are the units? :")

calc = int(user_input1) * unit_dict[user_input2]

print(f"{user_input1} {user_input2} is {calc} meters")
