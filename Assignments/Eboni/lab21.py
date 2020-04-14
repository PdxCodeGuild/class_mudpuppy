import string
with open("words1.txt", 'r') as f:
    for line in f.readlines():
        line = line.lower()
        for punc in string.punctuation:
            line = line.replace(punc, '')
        line_list = line.split() 
word_counter = {}
for word in line_list:
    if word_counter[line_list] == word_counter[line_list] + 1:
        print(word_counter)
       