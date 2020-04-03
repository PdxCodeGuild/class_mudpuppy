# double_letter_finder.py
s2 = "I have a book in my bag."
s1 = "I have a jacket in my bag."

# found_letter = ''
found_double_letter = False
for index in range(len(s1) - 1):
    # print(index, s1[index], index + 1, s1[index + 1])
    if s1[index] == s1[index + 1]:
        found_double_letter = True
        found_letter = s1[index] + s1[index + 1]
        break
if found_double_letter:
    print(f"It has double letters: {found_letter}")
else:
    print("It doesn't have double letters")