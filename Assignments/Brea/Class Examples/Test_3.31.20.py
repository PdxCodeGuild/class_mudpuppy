#Test for March 31st, 2020
# 
# military_gen.py
# user_letters = input("Give me some letters : ")

# mil_dict = {'a': 'alpha',
# 'b': 'bravo',
# 'c': 'charlie',
# 'd': 'delta',
# 'e': 'echo',
# 'f': 'foxtrot',
# 'g': 'golf'}

# output = ''

# for letter in user_letters:
#     output += mil_dict[letter] + ''
    
# print(output)


#lunch_order.py
#[number of sandwiches][number of soups][number of waters]
#342 means 3 sandwiches, 4 soups, 2 waters

input_order = int(input("What's the order? : "))
sandwich_num = input_order // 100
soup_num = (input_order % 100) // 10
water_num = input_order % 10

print(f"{sandwich_num} sandwiches, {soup_num} soups, and {water_num} waters")