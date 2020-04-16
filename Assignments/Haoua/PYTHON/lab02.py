'''
All for the 'Gram
Bitches love the 'Gram
Oh wait shit
Brr brr
Brr, brr, brr (aye)
Skrrt, skrrt
Roxanne
Roxanne
'''
# import random
# print("ROXANNE EASY REMIX")
# i = 0 #I would like to create an if function that will return 'Snap' if the input is snapchat
# list1 = []

# while i < 2: #I may need to remove the while statements, to ask guest to repeat the same social media platform they wrote in social
#     social = input("Enter a social media platform : ") #list of social = ['instagram', 'snapchat', 'facebook']
#     list1.append(social)
#     i = i + 1
# print(list1)
#     #socialr = input("Enter a social media platform : ")
#     # i = i + 1
# shit = input("Enter an expletive : ") 
# #list2 = ['shit', 'freak', 'darn']
# #list2.append(shit)
# b = 0
# while b < 2:
#     brr = input("Enter random sound : ") 
#     list2 = []
#     list2.append(brr)
#     b = b + 1
#  #list1 = ['brr', 'grr', 'woof']
#  #list1.append(brr) #use .append(brr) to add to the list if the input is not on the list.
# s = (f',  {brr} ,  {brr}')
# #brr2 = print(brr.capitalize() + {s}') wrong syntax do not use.
# #social2 = input('Repeat the social media platform : ')
#     #i = i + 1 #a.upper() syntax #wrong use .capitalize, .upper = Capslock
# social2 = social[-4:] #I want this to take the input and return ' accommpanied by the last 4 characters(would prefer letters) .

# print(f'All for the \'{list1[0].capitalize()}') #What would we do if we only want it to return the last for characters in an input? I tried slicing it using negative numbers but received a blank.
# print(f'Bitches love the \'{list1[1].capitalize()}') 
# #shit = input("Enter an expletive")
# print(f'Oh wait {shit}')
# print(brr.capitalize(), brr)
# print(brr.capitalize() + f'{s} (aye)')
# # x = "a string"
# # user_input = input("enter something pretty:")
# # print(x + ' is not a ' + user_input)
# # print(f'{x} is not a {user_input}')
import random
# x = "Please enter a social media platform, expletive, random sound, second random sound (IN THAT ORDER!) :"
user_input = input("Please enter a social media platform, expletive, random sound, second random sound (IN THAT ORDER! Separate using spaces only) :")
list1 = user_input.split()

print('you submitted', len(list1), 'answers')
print(f"All for the \'{list1[0][-4:]}\nBitches love \'{list1[0][-4:]}\nOh wait {list1[1]}\n{list1[2]}\n{list1[3]}")

answers1 = ['no', 'nah', 'im good', 'i\'m good', 'n', 'nope']
answers2 = ['yes', 'y', 'yessir', 'yeah', 'yah', 'ye', 'yeh']
q = user_input.split()

'''
i = 0 #flag

while i < 10: #it'll ask 9 questions
    if i == 5:
        break
        # print('woohoo')
    print(i)
    i+= i + 1
else:
    print('i finished normally')
# print('done')
'''
'''
# while i < 2: #I may need to remove the while statements, to ask guest to repeat the same social media platform they wrote in social
#     social = input("Enter a social media platform : ") #list of social = ['instagram', 'snapchat', 'facebook']
#     list1.append(social)
#     i = i + 1
# print(list1)
#     #socialr = input("Enter a social media platform : ")
#     # i = i + 1
'''
c = 0
x = "Please enter a social media platform, expletive, random sound, second random sound (IN THAT ORDER! Seperate using spaces only) :"
b = input ("Would you like to continue?").lower()
while c < 1:
    if b in answers2:
        input(f'{x}')
        c += c + 1
        print('you submitted', len(list1), 'answers')
        print(f"All for the \' {list1[0][-4:]}\nBitches love \' {list1[0][-4:]}\nOh wait {list1[1]}\n{list1[2]}\n{list1[3]}")
        continue
    else:
        print("Thank you for playing!")
        break
            
# for b in answers2:
#     input(f'{x}')
#     print('you submitted', len(list1), 'answers')
#     print(f"All for the \' {list1[0][-4:]}\nBitches love \' {list1[0][-4:]}\nOh wait {list1[1]}\n{list1[2]}\n{list1[3]}")
    
#     # b = input("Would you like to continue?")
#     # if b == answers2:
#     #     continue
# else:
#     print('Thank you for playing!')
# for answers2 in q:
#     input(f'{x}')
#     print('you submitted', len(list1), 'answers')
#     print(f"All for the \' {list1[0][-4:]}\nBitches love \' {list1[0][-4:]}\nOh wait {list1[1]}\n{list1[2]}\n{list1[3]}")
#     break
# elif answers1 = q:
#     print("Thank you for playing")
#     break

# if q == {answers2}:
#     print(f'{user_input}')
#     print('you submitted', len(list1), 'answers')
#     print(f"All for the \' {list1[0][-4:]}\nBitches love \' {list1[0][-4:]}\nOh wait {list1[1]}\n{list1[2]}\n{list1[3]}")
# elif q == answers1:
#     print('Thank you for playing!')
