# #Test Examples, April 14th, 2020

# my_str = 'ab,c d,ef g,hi' #split() divides things by a delimiter 
# my_list = my_str.split(',') #(in this case, a comma but could be anything)

# print(my_list)

# for piece in my_list:
#     print(piece)

# my_str2 = "Hello, how are you?!".replace('?!', '.')
# print(my_str2)

# #--------------
# #how to open a file
# import string

# filename = ''
# l1 = []     #we'll put words in here
# l2 = []     #we'll put words in here
# with open(filename, 'r') as f: #'r' denotes that we're reading the file
#     book_str = (f.read())   #gives us one massive string
#     book_lst = book_str.strip().split('\t')     #.strip is a string method, so have to import string, takes away whitespace

#     for word in book_lst:
#         pairs = (word.split(':'))   
#         print(pairs) 
#         if pairs[0] == 'l1':   #if the string starts with l1
#             l1.append(pairs[1])     # append word to l1, don't need to point at list first
#         else:
#             l2.append(pairs[1])
        
#     story_lst = l1 + l2

#-----------------
#list_to_dict.py

start_list = [['a', 'b', 'c'], ['d', 'e', 'f']]

end_goal = []

for one_list in start_list:
    #one_list
    print(one_list)
    one_dict = {}
    for index in [0, 1, 2]: #range(len(one_list)
        #one_list[index]
        one_dict[index] = one_list[index]
    #one_dict
    end_goal.append(one_dict)

print(end_goal)

# future_end_goal = [{0: 'a', 1: 'b', 2: 'c'}, {0: 'd', 1: 'e', 2: 'f'}]


