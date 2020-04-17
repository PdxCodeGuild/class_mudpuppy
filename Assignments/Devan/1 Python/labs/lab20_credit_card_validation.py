

def multiply_odds(num):
    """ Double every other element in the reversed list. """
    for n in range(0, len(num), 2):
        num[n] *= 2       # Double every other number.
    for n in range(len(num)):  # Subtract nine from numbers over nine.
        if num[n] > 9:
            num[n] -= 9
    sum_num = sum(num)    # Sum all values.
    return sum_num

def cc_validation(num):
    cc = num
    num = [int(i) for i in num]
    check_digit = num.pop(-1)   # Slice off the last digit.
    num.reverse()  # Reverse the digits.
    sum_num = multiply_odds(num)
    num = int(''.join(map(str, num)))
    print(check_digit, sum_num, num, cc)
    if sum_num % 10 == check_digit:    # Compare digit 2 and check digit.
        print(f"{cc} is a valid credit card")
    else:
        print(f"{cc} is not a valid credit card")



cc_validation('4574310529164973')
