'''
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Visualization of test data:
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def myfunc(data):
    peak_list = []
    valley_list = []
    index_list = list(range(len(data))) #allows us to keep track of the indexes. Gives a list in the range of 19.

    for i in index_list:#Allow us to loop until the 19 index #We can't get 'i' without a for loop.
    # print(i+1)
        if (i-1) in index_list and (i+1) in index_list:
            if data[i] >= data[i-1] and data[i] >= data[i+1]: #allows us to check previous and post index
                peak_list.append(i)
                # return peak_list
            if data[i] < data[i-1] and data[i] < data[i+1]: #allows us to check previous and post index
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
