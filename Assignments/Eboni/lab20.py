def Convert (string):
    li = string.split(" ")
    return li
str1 = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5"
# print(Convert(str1))
li = (Convert(str1))
l2 = []
for index in range (len(li)-1):
    # print(li[index])
    l2.append(int(li[index]))
# print(l2)
# print(li[-1])
check = int(li[-1])
l2 = l2[::-1]
# print(l2)
# l2 = (l2[::2]) 
# print(l2)
for index, number in enumerate(l2):
    if index % 2 == 0:
        l2[index] = number *2
    if l2[index] > 9:
        l2[index] = l2[index] - 9
# print(l2)
running_total = sum(l2)
# print(running_total)
if running_total % 10 == check:
    print(f"Your credit is approved")

    


