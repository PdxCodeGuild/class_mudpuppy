n = int(input("Enter how many numbers you wish to average: "))

a = []

for i in range(0,n):
    elem=int(input("Enter number: "))
    a.append(elem)
avg = sum(a)/n

print("Average of numbers in the list",round(avg, 2))