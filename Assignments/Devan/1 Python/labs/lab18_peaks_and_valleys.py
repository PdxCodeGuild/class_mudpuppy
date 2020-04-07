
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def find_peaks(data):
    """ Returns the indices of 'peaks', a number with a lower number on both the left and the right. """
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return peaks


def find_valleys(data):
    """ Returns the indices of 'valleys', a number with a higher number on both the left and the right. """
    valleys = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valleys.append(i)
    return valleys


def peaks_and_valleys(data):
    """ Compiles a single list of the peaks and valleys in order of appearance in the original data. """
    peaks_and_valleys = find_peaks(data) + find_valleys(data)
    return sorted(peaks_and_valleys)


print(find_peaks(data))
print(find_valleys(data))
print(peaks_and_valleys(data))
