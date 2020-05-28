# Test for April 2nd, 2020
#double_letter_finder.py

s1 = "I have a book in my bag."
s2 = "I have a jacket in my bag. "

found_letter = None

found_double_letter = False
for index in range(len(s1) - 1): #-1 stops the print loop from going out of range on next line
    if s1[index] == s1[index + 1]:
        found_double_letter = True
        found_letter = s1[index] + s1[index + 1]
        break
if found_double_letter == True:
    print(f"It has double letters: {found_letter}")
else:
    print("It doesn't have double letters")
    #print(index, s1[index], index + 1, s2[index + 1]) #compares index of characters in string sentence, with indexes of one character over


#Favorite_colors.py
favorite_colors = ['blue', 'purple', 'red']
color_guesses = []

for _ in favorite_colors:
    one_guess = input("Guess one of my favorite colors: ")
    color_guesses.append(one_guess.lower())
color_guesses.sort()
favorite_colors.sort()
if color_guesses == favorite_colors:
    print("Correct")
else:
    print("Incorrect")