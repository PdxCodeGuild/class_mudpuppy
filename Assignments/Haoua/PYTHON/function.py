'''def my_function(fname): #fname is the argument, functions can have as many arguments as possible. just separate with commmas.
    #When the function is called, we pass along a first name.
    print(fname + " Refsnes")#used inside the function to print the full name:
#shortened to args in Python documents
#parameter is a variable listed inside the parentheses in the function definition.
#argument is the value that are sent to the function when it is called

my_function("Emil") = prints Emil Refsnes
my_function("Tobias") = prints Tobias Refsnes
my_function("Linus") = prints Linus Refsnes

-----------------------------------------------------
if your function expects 2 arguments, you must call the function with 2 arguments,
not more and not less.
-----------------------------------------------------
'''
'''ARBITRARY ARGUMENTS, *args:
if you don't know how many arguments that will be passed into your function, add a *
before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly.
'''
'''
enter = int(input("What's your favorite numnber? (0-2) : "))
def my_function(*kids):
    print("Your youngest child will be named" + kids[2]) #Depending on which name I want I can choose from the index
my_function(" Emil", " Tobias", " Linus")#if we change 2 to enter, it still produces linus
'''
#------------------------------------------------------------------
'''KEYWORD ARGUMENTs: We can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
'''
'''def my_function(child3, child2, child1):
    print("The youngest child is" + child3)
my_function(child1 = " Emil", child2 = " Tobias", child3 = " Linus")
'''
#----------------------------------------------------------------------
'''ARBITRARY KEYWORD ARGUMENTS (keyword arguments **kwargs):
If you dont know how many keyword arguemtns will be passed into
your function, add two asterisk: ** before the parameter name
in the function definition.

This way the function will receive a dictionary of argurments, and can access the items
accordingly:'''

'''def my_function(**kid):
    print("His last name is " + kid["lname"]) #If we don't put quotes, python will give us a NameError: 'lname' not defined
my_function(fname = "Tobias", lname = "Refsnes")'''
#-----------------------------------------------------
'''DEFAULT PARAMETER VALUE: if we call the function without argument, it uses the default value:
'''
'''
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
'''
#--------------------------------------------------------------------------------
'''PASSING A LIST AS AN ARGUMENT - you can send any data types of 
argument to a function (string, number, list, dictionary, etc.) and it will be treated
as the same data type inside the function.

E.g if you send a LIST as an argument, it will still be alist when it reaches the function:
'''
# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)
#apple
#banana
#cherry

'''RETURN VALUES'''
# def my_function(x):
#     return 5 * x
# print(my_function(3)) = 15
# print(my_function(5)) = 25
# print(my_function(9)) = 45
#------------------------------------------------------------------
'''THE PASS STATEMENT'''
# function definitions cannot be empty, 
# but if you for some reason have a function
# definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
    pass
#----------------------------------------------------------------------------
Recursion means that a function calls itself. This has the benefit of
meaning that you can loop through data to reach a result.

BE CAREFUL WITH RECURSION - YOU CAN WRITE A FUNCTION THAT NEVER TERMINATES, 
OR ONE THAT USES EXCESS AMOUNTS OF MEMORY OR PROCESSOR POWER.

tri_c


