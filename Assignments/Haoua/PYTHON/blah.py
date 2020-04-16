'''
def my_add() #snake case because everything is add 
myAddAnotherLetterHere() #Camel case
this_is_snake_case #Snake case
my-add-another-letter-here #kabob case
'''
# def my_add(number_1, number_2):
#     a_sum = number_1 + number_2
#     return a_sum
#     a_sum = a_sum - 500
#     print(a_sum)

# another_sum = my_add("5", "6")
# print(another_sum)
'''
x = 5 #okay I need to have a certain about of bytes for the character 5
print(x) #

greeting = "Hello"
print(greetings) #Mutable data means it can change.
#Immutable data structures needed to avoid data races
#REACT uses a lot of immutable data structures
#ints, floats, strings and tuples are immutable.
#strings like lower, replace, and strip return copies of the string rather than the original
'''
'''
my_string = 'This is A sTriNg wiTh RaNdoM caPs'
my_lowered_string = my_string.lower()
print(my_string)
print(my_string.lower()) #immutable data isn't always what you want but it will save you time down the road.
'''
'''
x = 5
y = x
y +=2#using += is the same as saying y= y+2
print(x) #5
print(y) #7

x = ['apples', 'bananas', 'pears']
'''
# name = input('what is your name?')
# print(f'hello {name}')

m = 10
print(id(m))#each m has a diffirent value (10)
m += 1
print(id(m)) (11)
#if they have the same id that means the object is mutable.