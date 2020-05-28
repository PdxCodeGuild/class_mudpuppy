#Lab 17, Version 1 April 2nd, 2020
#Palindrome Checker

user_input = input("What is your word? : ")

def split(word):
    return list(word)

def reverse_word(lst):
    return lst[::-1]

my_word = split(user_input)

rev_word = reverse_word(split(my_word))

def char_compare(list1, list2):
    match_num = 0
    for index in range(len(list1)):
        if list1[index] == list2[index]:
            match_num += 1
    return match_num

def palindrome_func(num, lst):
    palindrome_check = False
    if num == len(lst):
        palindrome_check = True
        print("This word is a palindrome.")
    else:
        print("This word is not a palindrome.")
    return palindrome_check

palindrome_func(char_compare(my_word, rev_word), my_word)
