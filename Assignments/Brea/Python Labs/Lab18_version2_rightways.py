pv_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


for y_coord in reversed(range(1, 21)): # for each row I'm printing starting at top row #1 to bottom row #max_height
    current_height = y_coord    #moves from top row, sequentially down to bottom row as for loop moves through range
    for index in range(len(pv_data)):   # runs through each column/index L to R (i.e., len of dataset) within the particular row I'm currently in
        current_position = index    # points at a specific coordinate within my full image grid
        block_height_at_this_index = pv_data[index]     #pulls number from dataset to set expectation of whether to print an x or not
        if block_height_at_this_index >= current_height: #compares whether current num from list. if num from list[index] is >= the row we're on (i.e., y coord), then prints an X in this exact coordinate
            print('X', end=' ')
        else:
            print(' ', end=' ')
    print() #prints out one row at at a time given each column as it moves across whatever row that y_coord is pointing to 
