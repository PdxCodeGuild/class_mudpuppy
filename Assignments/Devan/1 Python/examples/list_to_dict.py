start_list = [['a', 'b', 'c'], ['d', 'e', 'f']]

endgoal = []
one_list = []

for one_list in start_list:
    one_dict =  {}
    for i in range(len(one_list)):
        one_dict[i] = one_list[i]
    endgoal.append(one_dict)

print(endgoal)
