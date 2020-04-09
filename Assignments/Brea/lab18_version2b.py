#Lab 18, version 2 solution April 8th, 2020

pv_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


for y_coord in reversed(range(1, 21)):
    current_height = y_coord
    for x_coord in range(len(pv_data)):
        current_position = x_coord
        mountain_height_at_current_position = pv_data[x_coord]
        if mountain_height_at_current_position >= current_height: #same thing as inkscape starting from top row
            print('X', end=' ')
        else:
            print(' ', end=' ')
    print()