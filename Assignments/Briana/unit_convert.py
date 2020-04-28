# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

# > what is the distance in feet? 12
# > 12 ft is 3.6576 m

# users_num = int(input('How many feet would you like converted into meters? '))

# meters = str((users_num)*0.3048)

# print(meters)



# Version 2
# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.


# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m
# Below is some sample input/output:

# users_unit = input('What unit of measurement would you like converted into meters? (feet, miles, meters, kilometers)')
# users_num = int(input(f'How many {users_unit} would you like converted into meters? '))

# if users_unit == "feet":
#     meters = str((users_num)*0.3048)
# if users_unit == "miles":
#     meters = str((users_num)*1609.34)
# if users_unit == "meters":
#     meters = str((users_num)*1)
# if users_unit == "kilometers":
#     meters = str((users_num)*1000 )
# print(meters)
    
# if users_unit != 'feet' or 'miles' or 'meters' or 'kilometers':
#     wrong_input = input("Please enter valid unit ")





# Version 3
# Add support for yards, and inches.

# 1 yard is 0.9144 m
# 1 inch is 0.0254 m


# users_unit = input('What unit of measurement would you like converted into meters? (inches, feet, yards, meters, kilometers, miles)')
# users_num = int(input(f'How many {users_unit} would you like converted into meters? '))

# if users_unit == "feet":
#     meters = str((users_num)*0.3048)
# if users_unit == "miles":
#     meters = str((users_num)*1609.34)
# if users_unit == "meters":
#     meters = str((users_num)*1)
# if users_unit == "kilometers":
#     meters = str((users_num)*1000 )
# if users_unit == "yards":
#     meters = str((users_num)*0.9144 )
# if users_unit == "inches":
#     meters = str((users_num)*0.0254 )

# print(meters)





# Version 4
# Now we'll ask the user for the distance, the starting units, and the units to convert to.

# You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

# ft	mi	m	km
# ft	1		0.3048	
# mi		1	1609.34	
# m	1/0.3048	1/1609.34	1	1/1000
# km			1000	1
# But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

# Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

# Below is some sample input/output:



get_distance = int(input('Enter value to be converted: '))
user_input = input('Enter starting unit ') 
user_output = input('Enter ending unit ')

# [ft	mi	m	km]
# [ft	1		0.3048]	
# [mi		1	1609.34]	
# [m	1/0.3048	1/1609.34	1	1/1000]
# [km			1000	1]]

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m

measure_dict = {    
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.91,
    "meters": 1,
    "miles": 1609.34,
    "kilometers": 1000,}
    



result = (get_distance*((measure_dict[user_input])/measure_dict[user_output]))


print(result)