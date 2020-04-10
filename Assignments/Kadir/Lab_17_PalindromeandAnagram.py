#Lab_17_PalindromeandAnagram

import string 


enter = input("enter the first word: ")

rev_string = enter[::-1]


print("reversed version: ", rev_string + " :")


def myfunction(enter):

    if enter == rev_string:

        print("This is a palindrome")

    else: 

        print("this is not a palindrome")

myfunction(enter)



#part 2:




w1 = input("Enter the first word : ")

exclude = set(string.punctuation)

w1 = ''.join(ch for ch in w1 if ch not in exclude).replace(" ","")


w2 = input("Enter the Second word : ")

exclude = set(string.punctuation)

w2 = ''.join(ch for ch in w2 if ch not in exclude).replace(" ", "")


def myfunction_(w1, w2):

    if sorted(list(w1)) == sorted(list(w2)):

        print(f"{w1} and {w2} are anagrams.".lower())

    else:

        print(f"{w1} and {w2} aren't anagrams".lower())

myfunction_(w1, w2)