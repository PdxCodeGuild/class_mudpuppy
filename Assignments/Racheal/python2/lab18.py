data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# a = [6, 14] 
# # index
# a = [9, 17]
# # peaks and valleys (data)
# a = [6, 9, 14, 17]


# def find_highest_number(A):
#     pass

def myfunc(data):
    peak_list = []
    valley_list = []
    index_list = list(range(len(data))) #this helps with keeping the indexes organized.(range of 19)

    for i in index_list:#this allows for the function to loop 19 times..... for-loop will only be created with 'i'
    # print(i+1)
        if (i-1) in index_list and (i+1) in index_list:
            if data[i] >= data[i-1] and data[i] >= data[i+1]: #here we can check the last index 
                peak_list.append(i)
                # return peak_list
            if data[i] < data[i-1] and data[i] < data[i+1]: #here we can check the last and the following 
                valley_list.append(i)
    return (f"Peaks List: {peak_list} \nValleys List : {valley_list} \nBoth : {valley_list + peak_list}")
print(myfunc(data))


print("                             X           X ")
print("                           X X X       X X ")
print("             X           X X X X X   X X X ")
print("           X X X       X X X X X X X X X X ")
print("         X X X X X   X X X X X X X X X X X ")
print("       X X X X X X X X X X X X X X X X X X ")
print("     X X X X X X X X X X X X X X X X X X X ")
print("   X X X X X X X X X X X X X X X X X X X X ")
print(" X X X X X X X X X X X X X X X X X X X X X ")
print("[1 2 3 4 5 6 7 6 5 4 5 6 7 8 9 8 7 6 7 8 9]")

print(myfunc(data))


print()