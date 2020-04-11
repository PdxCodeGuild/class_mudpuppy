#Lab 18, version 3, April 7th, 2020

pv_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

water_units = 0

for y_coord in reversed(range(1, (len(pv_data)))):
    current_height = y_coord
    for index in range(len(pv_data)):
        current_position = index 
        block_height_at_this_index = pv_data[index]     
        if block_height_at_this_index >= current_height: 
            print('X', end=' ')
        else:
            print(' ', end=' ')
    print()

water_units = 0

for y_coord in reversed(range(1, (len(pv_data)))):
    current_height = y_coord
    for index in range(len(pv_data) - 1):
        current_position = index 
        right_position = [index+1]

        if right_position < current_position:
            water_units += 1

    print(water_units)