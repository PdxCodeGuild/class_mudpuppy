import string
word_counter = {}
with open("words1.txt", 'r') as f:
    for line in f.readlines():
        line = line.lower()
        for punc in string.punctuation:
            line = line.replace(punc, '')
        line_list = line.split() 
        print(line_list)
        for word in line_list:
            if word in word_counter.keys():
                word_counter[word] = word_counter[word] + 1
            else:
                word_counter[word] = 1
print(word_counter)
words = list(word_counter.items())
def return_index_one(in_tup):     
    return in_tup[1]
words.sort(key=return_index_one, reverse = True)
for i in range(min(10, len(words))):
    print(words[i])