#lab21_count_words.py

import string
word_dict = {}

with open("lab21_book.txt", 'r', encoding = "utf8") as f: # opening the file and naming the variable "f"
    for line in f.readlines(): # breaks the code into lines by \n
        line = (line.lower())  # make strings lowercase

        for c in string.punctuation:  # loops over punctuation
            line = line.replace(c, "")  # removes punctuation

        line_of_words = (line.split()) # separating the words in the text
        
        for word in line_of_words:
            if word in word_dict.keys():
                word_dict[word] = word_dict[word] + 1 # add and count it
            else:
                word_dict[word] = 1 # leave it at the same number, don't add

print(word_dict)

text_words = list(word_dict.items()) # .items() returns a list of tuples
text_words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(text_words))):  # print the top 10 words, or all of them, whichever is smaller

     print(text_words[i])            