nums = [5, 0, 8, 3, 4, 1, 6] # the starting array of nums
running_sum = 0 #to start need an int of 0 to be able to add 
for num in nums:# looping through the list
    running_sum = running_sum + num #when looping we are adding and changing out runningsum var ex: 5+runningsum which = 0 will change running sum to 5
    
num_avg = running_sum / (len(nums)) #mathy stuff that gives us the average
print(f'The average of your numbers is {num_avg}') #print our average

