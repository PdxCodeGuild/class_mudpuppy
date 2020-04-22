filename = 'story_weird_format.txt' # the file to open
l1 = [] # we'll put words in here
l2 = [] # we'll put words in here
with open(filename, 'r') as f: # f is the file
    book_str = f.read()
    book_lst = book_str.strip().split('\t') # remove white space and split on tab
    for word in book_lst:
        pairs = word.split(':')
        if pairs[0] == 'l1':
            l1.append(pairs[1])
        else:
            l2.append(pairs[1])
        # if the string start with l1
            # append word to l1
print(l1, l2)
