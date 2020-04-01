# lunch_order.py

# [number of sandwiches][number of soups][number of waters]
# 342 -> 3 sandwiches, 4 soups, 2 water

input_order = int(input("What's the order? "))
sandwich_num = input_order // 100
soup_num = (input_order % 100) // 10
water_num = input_order % 10
print(f"{sandwich_num} sandwiches, {soup_num} soups, {water_num} waters.")