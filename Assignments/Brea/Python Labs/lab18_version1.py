#Lab18, version 1 April 6th, 2020

pv_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data_list):    #returns indices of peaks, lower nums on L and R
    peak_list = []
    for index in range(1, len(data_list)-1):
        left_side = data_list[index-1]
        middle = data_list[index]
        right_side = data_list[index+1]

        if (left_side < middle and right_side < middle):
            peak_list.append(index)
    return peak_list

def valleys(data_list):
    valley_list = []
    for index in range(1, len(data_list)-1):
        left_side = data_list[index-1]
        middle = data_list[index]
        right_side = data_list[index+1]

        if (left_side > middle and right_side > middle):
            valley_list.append(index)
    return valley_list

def peaks_and_valleys(list1, list2):
    peaks_valleys_list = list1 + list2
    peaks_valleys_list = sorted(peaks_valleys_list)
    return peaks_valleys_list


peaks_output = (peaks(pv_data))
print(peaks_output)
valleys_output = (valleys(pv_data))
print(f"The peaks are at indices {peaks_output} and the valleys are at {valleys_output}")

print(peaks_and_valleys(peaks(pv_data), valleys(pv_data)))