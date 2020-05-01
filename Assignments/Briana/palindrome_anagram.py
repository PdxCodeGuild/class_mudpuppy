# # while True:
# user_input = input("Enter word: ")
 
# # print(len(user_input))
 
# if (user_input) == (user_input[::-1]):
#     print('palindrome')
# else:
#     print('noope!')

 
 
# OR
 
# ast = input('Tell me a word of your choice: ')
# last = len(ast)
# rast = ""
# for i in range(last):
#     rast += ast[last-1-i]
#     print(rast)


# Anagram

user_input = input("Enter word 1 ")
 
user_input2 = input ("Enter Word 2 ")
 
input_1 = user_input.replace(" ", "")
 
input_2 = user_input2.replace(" ", "")
 
print(input_1)
 
print(input_2)
 
sort1 = sorted(input_1)
 
sort2 = sorted(input_2)
 
print(sort1)
 
print(sort2)
 
if sort1 == sort2:
    print("Anagram!")
   
else:
    print("Better Luck Next Time")