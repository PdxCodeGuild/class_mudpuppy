# def double doubles whole string of numbers. How to only double every other number. and How to insert the reversed cc number into the double function
# cc_number = 4556737586899855

def string_to_list(cc_number):
    cc_number = list(cc_number)
    for i in range (len(cc_number)):
        cc_number[i] = int(cc_number[i])
    return cc_number
# print(string_to_list("4556737586899855"))

def double(cc_number_list):
    for i in range(0, len(cc_number_list), 2):
        cc_number_list[i] *= 2
    return cc_number_list
# print(double([589986857376554]))    
# print(double([589986857376554]))

def subtract_nine(cc_number_list):
    for i in range(len(cc_number_list)):
        if cc_number_list[i] > 9:
            cc_number_list[i] -= 9
    return cc_number_list


def second_digit(number):
    return int(list(str(number))[1])

def check_valid(x, y):
    if x == y:
        print('CC number valid')
    else:
        print('CC number invalid')

def cc_validation(cc_number):
    cc_number = string_to_list(cc_number)
    check_digit = cc_number.pop()
    cc_number.reverse()
    cc_number = double(cc_number)
    cc_number = subtract_nine(cc_number)
    sum_nums = sum(cc_number)
    digit2 = second_digit(sum_nums)
    check_valid(digit2, check_digit)

def main():
    cc_number = '4556737586899855'
    # credit_card = input("Input cc number: ")
    cc_validation(cc_number)

main()




# print(check_digit)
# print(cc_number.reverse())
# print(double(cc_number))
# print(subtract_nine(cc_number))
# print(sum(cc_number))
# print(second_digit(sum_nums))
# print(cc_number)
# print(string_to_list)
# print(double)
# print(subtract_nine)
# print(second_digit)
# print(check_valid)
# print(cc_validation)


# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!