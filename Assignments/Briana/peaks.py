# data = []
# data = ["1", "2", "3", "4" , "5" , "6" , "7" , "6" , "5" , "4" , "5" , "6" , "7" , "8" , "9" , "8" , "7" , "6" , "7" , "8" , "9"]

# i = 0
# while i < 20:
#     print(list(i))
#     if i >= 20:
#         break
#     i += 1

#     for i in data:
#         x = (data.index(i) + 1)
        
#         y = (data.index(i) - 1)

#     if x < data.index(i) and y < data.index(i):
#         print("peak")pwd

#     if x > data.index(i) and y > data.index(i):
#         print("valley")




# while (True):               # <- infinite while loop
#     lo += 1
#     for i in range(len(l)): # <- for loop
#         if not l[i] < 3:
#             break           # <- break the for loop
#         print(lo)

# # attempt 2:


#         data = []
# data = ["1", "2", "3", "4" , "5" , “6” , “7” , “6” , “5” , “4” , “5” , “6” , “7” , “8” , “9” , “8” , “7” , “6” , “7” , “8” , “9”]

# i = 1
# while i < 3:
# 	print(i)
# 	if i >= 3:
#     	break
# 	i += 1

# for i in data:
# 	x = (data.index(i) + 1)
	
# 	y = (data.index(i) - 1)

# if x < data.index(i) and y < data.index(i):
# 	print("peak")

# if x > data.index(i) and y > data.index(i):
# 	print("valley")


# attempt 3: 



test_data = ['5', '6', '7', '6', '5', '4', '5', '6', '7', '8', '9', '8', '7', '6', '7', '8', '9']


def main():
    peaks_list = peaks(test_data)
    valleys_list = valleys(test_data)
    peaks_and_valleys_list = peaks_and_valleys(test_data)
    print('Data: ', test_data, 'Peaks list: ', peaks_list, '\nValleys list: ', valleys_list, '\nPeaks and Valleys list: ', peaks_and_valleys_list)
    return 'Data: ', test_data, 'Peaks list: ', peaks_list, 'Valleys list: ', valleys_list, 'Sorted Peaks and Valleys list: ', peaks_and_valleys_list


def peaks(list_data):
    peaks_list = list()
    for idx, val in enumerate(list_data):
        if len(list_data) - 1 > idx > 0:
            if list_data[idx-1] < val > list_data[idx+1]:
                peaks_list.append(val)
                # print('Peak found ', peaks_list)

    # print('peak list is ', peaks_list)
    return peaks_list


def valleys(list_data):
    valley_list = list()
    for idx, val in enumerate(list_data):
        if len(list_data) - 1 > idx > 0:
            if list_data[idx - 1] > val < list_data[idx + 1]:
                valley_list.append(val)
                # print('Peak found ', valley_list)

    # print('peak list is ', valley_list)
    return valley_list


def peaks_and_valleys(sample_data):
    # Convert items in list to integers
    parsed_list = list(map(int, sample_data))

    # Create dictionary of peaks with key: index, value: value
    peaks_list = peaks(parsed_list)

    # Create dictionary of valleys with key: index, value: value
    valleys_list = valleys(parsed_list)

    master_list = list()
    for i in peaks_list:
        master_list.append(i)

    for i in valleys_list:
        master_list.append(i)

    return sorted(master_list)


if __name__ == '__main__':
    main()