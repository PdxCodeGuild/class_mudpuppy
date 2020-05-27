# #wacky_functions.py

# def noisy_add(num1, num2):
#     print(f"ADDING {num1} AND {num2}!!!! :D")
#     return num1 + num2

# def bad_add(num1, num2):
#     print(num1 + num2)

# print(bad_add(1, 3) + (-2, 5))

# print (noisy_add(noisy_add(1, 3), noisy_add(-2, 5)))

# def print4(in_thing): #same thing you pass in is the same thing it returns (thing in parenthesis )
#     print(4)
#     return in_thing

# def return4(in_thing):
#     print(in_thing)
#     return 4

# var1 = print4('a') + print4('b')
# print(var1)
# var2 = return4('a') + return4('b')
# print(var2)

while True:
    user_input = input("Please type cat: ")
    if user_input == 'cat':
        break
    else:
        print('not cat')