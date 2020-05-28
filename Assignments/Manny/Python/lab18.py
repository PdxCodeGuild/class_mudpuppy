import string
input_string = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
for index in range(1,len(input_string)-1):
    leftside = input_string[index-1]
    middle = input_string[index]
    rightside = input_string[index + 1]
    if leftside < middle and rightside < middle:
        print(index)
    elif leftside > middle and rightside > middle:
        print(index)