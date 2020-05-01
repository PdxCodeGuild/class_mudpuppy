# # Version 1
# import  math

# num = int(input('enter number '))

# q = 25
# d = 10
# n = 5
# p = 1


# number_q = str((num)//q)

# print ( 'Number of Quarters = ' + number_q )

# remainder_q = ((num)%q)

# # print (remainder_q)

# number_d = str(remainder_q//d)

# print ('Number of Dimes = ' + number_d)

# remainder_d = remainder_q%d

# # print (remainder_d) 

# number_n = str(remainder_d//n)

# print ('Number of Nickels = ' + number_n)

# remainder_n = remainder_d%n

# # print (remainder_n)


# number_p = str(remainder_n//p)

# print('Number of Pennies = ' + number_p) 


# Version 2 

import  math

num = float(input('enter dollar amount: '))

q = .25
d = .10
n = .05
p = .01


number_q = str((num)//q)

print ( 'Number of Quarters = ' + number_q )

remainder_q = ((num)%q)

# print (remainder_q)

number_d = str(remainder_q//d)

print ('Number of Dimes = ' + number_d)

remainder_d = remainder_q%d

# print (remainder_d) 

number_n = str(remainder_d//n)

print ('Number of Nickels = ' + number_n)

remainder_n = remainder_d%n

# print (remainder_n)


number_p = str(remainder_n//p)

print('Number of Pennies = ' + number_p) 