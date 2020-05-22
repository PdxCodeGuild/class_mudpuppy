# doesnt work:
# user_input = []
# user_input = list(input("Enter text to be encrypted: "))

# print(list(user_input))
   
# dict = {
#     'a' :  'n'  ,
#     'b' :  'o'  ,
#     'c' :  'p'  ,
#     'd' :  'q'  ,
#     'e' : ' r ' ,
#     'f' : ' s ' ,
#     'g' : ' t ' ,
#     'h' : ' u ' ,
#     'i' : ' v ' ,
#     'j' : ' w ' ,
#     'k' : ' x ' ,
#     'l' : ' y ' ,
#     'k' : ' z ' ,
#     'n' : ' a ' ,
#     'o' : ' b ' ,
#     'p' : ' c ' ,
#     'q' : ' d ' ,
#     'r' : ' e ' ,
#     's' : ' f ' ,
#     't' : ' g ' ,
#     'u' : ' h ' ,
#     'v' : ' i ' ,
#     'w' : ' j ' ,
#     'x' : ' k ' ,
#     'y' : ' l ' ,
#     'z' : ' m ' }   

# print(dict.get(list(user_input)))

# version 1 


import string

characters = list(string.ascii_lowercase)

user_input = input("Enter text to be encrypted:  ")

# rotation = int(input("Enter your rotation "))

input = list(user_input)

y = []

for i in input:

    if i in characters:

        x = (characters.index(i) + 13) % 26

        y += characters[x]

    else:

        y.append(i)

y = "".join(y)

print(str(y))





# version 2
# import string

# characters = list(string.ascii_lowercase)

# user_input = input("Enter text to be encrypted:  ")

# rotation = int(input("Enter your rotation "))

# input = list(user_input)

# y = []

# for i in input:

#     if i in characters:

#         x = (characters.index(i) + rotation) % 26

#         y += characters[x]

#     else:

#         y.append(i)

# y = "".join(y)

# print(str(y))
