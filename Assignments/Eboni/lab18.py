import string
input_string = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9] #change variable name
#create an empty list
for index in range(1,len(input_string)-1):
    left_side = input_string[index-1]
    middle = input_string[index]
    right_side = input_string[index + 1]
    if left_side < middle and right_side < middle:
        print(index)
    elif left_side > middle and right_side > middle:
        print(index)

