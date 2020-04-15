# list_to_dict.py
start_list = [['a', 'b', 'c'], ['d', 'e', 'f']]

output = []
for one_list in start_list:
    # one_list = ['a', 'b', 'c']
    print(one_list)
    one_dict = {}
    for index in [0, 1, 2]:#range(len(one_list)):
        #index = 0
        #one_list[index] = 'a'
        one_dict[index] = one_list[index]
    # one_dict = {0: 'a', 1: 'b', 2: 'c'}
    output.append(one_dict)

print(output)
# [{0: 'a', 1: 'b', 2: 'c'}, {0: 'd', 1: 'e', 2: 'f'}]
'''
endgoal = [
    {0: 'a',
    1: 'b',
    2: 'c'},
    {0: 'd',
    1: 'e',
    2: 'f'}
]
print(endgoal)
'''