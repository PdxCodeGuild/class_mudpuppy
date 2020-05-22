import string
print(string.ascii_lowercase.index('a'))

unencoded = 'helloiliketocode'
num_list = []
for letter in unencoded: 
    num = string.ascii_lowercase.index(letter)
    num_list.append(num)

print(num_list)

for num in num_list:
    print(string.ascii_lowercase[(num+1) % len(string.ascii_lowercase)])

encoded = ''

for num in num_list:
    index = (num + 13) % len(string.ascii_lowercase)
    encoded += string.ascii_lowercase[index]

print(encoded)