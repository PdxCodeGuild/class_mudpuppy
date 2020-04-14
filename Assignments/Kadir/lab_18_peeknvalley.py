#lab_18_peeknvalley
#Finding number of data and also using functions  

import time

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# iterates through item passed into the function to check to see if the value at the index is > than both the left and right value at its position. If that is TRUE then it updates the "peaks" dictionary with the index or key of that value.
def peaks(x):
    peaks = {}
    for i in range(1,len(x)-1):
        if (x[i-1]) < x[i] and x[i] > (x[i+1]):
            peaks.update({i : x[i]})  
    return list(peaks.keys())

def valleys(x):
    valleys = {}
    for i in range(1,len(x)-1):
        if (x[i-1]) > x[i] and x[i] < (x[i+1]):
            valleys.update({i : x[i]})
    return list(valleys.keys())

def peaks_valleys(x):
    return sorted(valleys(x) + peaks(x))

print(data)
print(peaks(data))
print(valleys(data))
print(peaks_valleys(data))

def landscaping(x):
    v = max(x)
    print(f"The highest peak is a value: {v}!")
    while v > 0:
        time.sleep(.75)
        for i in range(len(x)-1):
            if x[i] < v:
                print(" ", sep=" ", end=" ")
            elif x[i] == v:
                print("X", sep=" ", end=" ")
            elif x[i] > v:
                print("X", sep=" ", end=" ")
        print()
        v -= 1

landscaping(data)