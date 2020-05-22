import string
unencoded = "helloiliketocode"
unencoded = "uryybvyvxrgbpbqr"
num_list = []
for letter in unencoded:
    num = string.ascii_lowercase.index(letter)
    num_list.append(num)
encoded = ''
for num in num_list:
    index = (num + 13) % len(string.ascii_lowercase)
    encoded += string.ascii_lowercase[index]
print(encoded)
