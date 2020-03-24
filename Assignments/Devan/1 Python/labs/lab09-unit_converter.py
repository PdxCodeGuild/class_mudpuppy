'''
This lab will involve writing a program that allows the user to convert a number between units.

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
'''

d_units = {'ft': .3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'yd': 0.9144, 'in': 0.0254}
user_distance = int(input('Enter a distance: '))
input_unit = input('What are the units? ')

if d_units.keys():
    output_distance = user_distance * d_units[input_unit]
    print(f'{user_distance} {input_unit} is {output_distance} m.')
else:
    print('Something went wrong.')
