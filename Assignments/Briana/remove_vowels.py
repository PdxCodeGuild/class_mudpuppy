import string
abc_list = list(string.ascii_lowercase)
vowels = 'aoeuiy'
for index in reversed(range(len(abc_list))):
    if abc_list[index] in vowels:
        print(f"Removing {abc_list.pop(index)}")
print(abc_list)