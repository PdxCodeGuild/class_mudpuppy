# word_info.py
import string
book = "\nSee spot run. Spot runs fast. Run spot, run!\n"
book = book.strip().lower()
for punc in string.punctuation:
    book = book.replace(punc, '')
book_l = book.split()

word_counter = {}
for word in book_l:
    if word in word_counter.keys():
        word_counter[word] += 1
        # word_counter[word] = word_counter[word] + 1
        # increment word (weird syntax)
    else:
        word_counter[word] = 1
        # count the word for the first time

# PART 2
word_list = list(word_counter.items())


print(word_list)

while True:
    user_choice = input("Choose (w)ord, (n)umber, or (d)one: ")
    if 'w' == user_choice:
        user_word = input("Give me the word: ")
        for word_tup in word_list:
            if word_tup[0] == user_word:
                print(word_tup)
    elif 'n' == user_choice:
        user_num = int(input("Give me the number: "))
        for word_tup in word_list:
            if word_tup[1] == user_num:
                print(word_tup)
    elif 'd' == user_choice:
        break
    else:
        print("What?")
