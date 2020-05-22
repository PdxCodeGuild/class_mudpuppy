
input_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peak(input_data):
    peak = []
    for index in range(1, len(input_data) -1):
        left_side = input_data[index -1]
        middle = input_data[index]
        right_side = input_data[index + 1]

        if middle > left_side and middle > right_side:
            peak.append(index)
            
    return peak
print(peak(input_data))


def valley(input_data):
    valley = []
    for index in range(1, len(input_data) -1):
        left_side = input_data[index -1]
        middle = input_data[index]
        right_side = input_data[index + 1]

        if middle < left_side and middle < right_side:
            valley.append(index)
            
    return valley
print(valley(input_data))


def peak_and_vally(input_data):
    peak_and_vally = []
    for index in range(1, len(input_data) -1):
        left_side = input_data[index -1]
        middle = input_data[index]
        right_side = input_data[index + 1]

        if (middle > left_side and middle > right_side) or (middle < left_side and middle < right_side):
            peak_and_vally.append(index)
            
    return peak_and_vally
print(peak_and_vally(input_data))
