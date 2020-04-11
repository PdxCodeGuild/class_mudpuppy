pv_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

block = 'X'

def print_new_line(num):
        print(block * num)
        return (block * num)

for piece in pv_data:
    print_new_line(piece) 