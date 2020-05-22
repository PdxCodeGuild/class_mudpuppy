
import random
#Twinkle, twinkle, little star,
#How I wonder what you are!
#Up above the world so high,
#Like a diamond in the sky.



# little = input("Enter adjective:")
# wonder = input("Enter verb:")
# world = input("Enter noun:")
# high = input("Enter adjective:")
# diamond = input("Enter noun:")
# sky =input("Enter noun:")

# print(f"twinkle, twinkle,{little} star, how I {wonder} what you are! Up above the {world} so {high} like a {diamond}in the {sky}. Twinkle twinkle little start, how I wonder what you are")

# list1 = []

user_input = input('enter a plural noun, an adjective, a verb, a noun, and another adjective:' )
# list1 = user_input.append(user_input)

# print(f"twinkle, twinkle,{little} star, how I {wonder} what you are! Up above the {world} so {high} like a {diamond}in the {sky}. Twinkle twinkle little start, how I wonder what you are")

user_input_list = user_input.split()
print(len(user_input_list))
print(f"twinkle, twinkle,{user_input_list[0]} star, how I {user_input_list[1]} what you are! Up above the {user_input_list[2]} so {user_input_list[3]} like a {user_input_list[4]}in the. Twinkle twinkle little start, how I wonder what you are")

word = ""
for i in range():
    word += random.choice()
    print(word)