#Test Examples April 21st, 2020

#average numbers lab re-do

# nums = [5, 0, 8, 3, 4, 1, 6]

# running_sum = 0

# for num in nums:
#     running_sum = running_sum + num
#     print(running_sum)

# aver = running_sum / len(nums)

# print(f"The average of your numbers is {aver}.")

#--------REPL Version of average numbers lab
# nums = []
# running_sum = 0

# while True:
#     user_input = int(input("Enter a number (or, '0' for done) : "))
#     if user_input == 0:
#         aver = running_sum / len(nums)
#         print(f"The average of your numbers is {aver}.")
#         break
#     nums.append(user_input)
#     running_sum += user_input
#     print(nums)

#-----------class version of average numbers

# class NumList:
#     def __init__(self):
#         self.nums = []
    
#     def append(self, in_num):
#         self.nums.append(int(in_num))
    
#     def average(self):
#         return sum(self.nums) / len(self.nums)

# me = NumList()

# while True:
#     user_input = input("Enter a number or 'done': ")
#     if user_input == 'done':
#         break
#     me.append(user_input)

# print(me.nums)
# print(me.average())

#---------------------
#Tic Tac Toe Tests
board = [[' ', '|', ' ', '|', ' '], 
        [' ', '|', ' ', '|', ' '],
        [' ', '|', ' ', '|', ' ']]

board2 = []

    
# for inner_list in board:
#     board2.append(''.join(inner_list))

board2 = '\n'.join([''.join(inner_list) for inner_list in board])
print(board2)


    


