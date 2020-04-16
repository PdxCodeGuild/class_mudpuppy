# '''
# drawing shapes onto the string
# We are giving the computer a set of instructions
# The more complex instructions the more complex the tax
# '''

# # print("   /|") #Computer executes each in order
# # print("  / |")
# # print(" /  |")
# # print("/___|")

# '''Variables in Python'''
# character_name = " John"
# character_age = 50
# is_male = False #(Boolean value)
# print("There once was a man named" +  character_name + ", ") or (f'There once was a man named {character_name}') #change the name and age in the story
# print("he was 70 years old.")
# print("He really liked the name George,")
# print("but didn't like being 70.")
# #Variable will store name and age in program #separate two words with an underscore

# '''Strings'''
# phrase = "so is solange."
# print("Beyonce is\n a bad bitch" + phrase)
# print(phrase.lower()) #used to convert phrase string to lower case
# print(phrase.isupper()) #gives me a false value because it is not all upper case
# print(phrase.upper().isupper()) #convert everything to uper case than let me know if it is upper.
# print(len(phrase)) #how many characters are inside the string.
# #imagine if we want to grab just one character
# print(phrase[0]) #gives us s
# print(phrase.index(s)) #tells us where a character is (0)
# print(phrase.index("sola"))
# print(phrase.replace("Beyonce", "Solange")) #replaces beyonce with solange


# '''numbers'''
# '''
# print(80)
# print(3 * (4 + 5)) #it will add 4 and 5 first because we used parenthesis to classify order of operations
# print( 10 % 3) #takes first number and divides by second number. it gives us a remainder . Read as 10 mod 3
# my_num = 5
# print(my_num) 
# print(str(my_num) + " my favorite number") #converts value into a string
# '''
# my_num = -5
# print(abs(my_num)) #This returns the absolute value.
# '''---------------------------------------------------------------------------------------------------------------------------------------'''
# print(pow(5,3)) #allows us to give it to pieces of number. It takes the first number (5) and raises it to the power of (3). LOOKS: 5^3
# print(max(4,6)) #will print out the max of two objects. OUTPUT: 6 because it is the larger of the two.
# print(min(4,6)) #will print out the min of two obects. OUTPUT: 4 because it is the smaller of the two
# print(round(3.2)) #Allows us to round a number. Rounds to 3.

# '''importing: in order to access other numbers. We can import external code into our file.'''
# from math import * #Go out and grabs a bunch of different math functions we can use. In order to access them we need to include this in our file
# #gives us access to more functions and allows us to do more with math. (Search different math functions).
# my_num = -5
# print(floor(3.7)) #grabs the lowest number (chops off the decimal number) (3)
# print(ceil(3.7)) #rounds up no matter what (4)
# print(sqrt(36)) #returns the square root of a number. (6)


''' Madlibs Lab '''
# color = input("Enter a color")
# plural_noun = input("Enter a plural noun")
# celebrity = input("Enter a celebrity")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

'''Lists''' #a structure we can use to store information.
# friends = ["Mahlet", "Racheal", "Elizabeth", "Fahad", "Lydia"] #stores multiple values inside the same object. We can change one to a number or a Boolean and it won't matter.
# friends[1] = "Chinyere" #if I want to change Racheal's name to Chinyere's.
# print(friends) #Each friend name is an element. Lets say we want to print one element in the list. Each one has an index starting at (0)
# print(friends[0]) #if we use negatives it starts from the back of the list. The first one in the back of the list starts at -1.
# print(friends[1:]) #grabs index 1 and everything after it.
# print(friends[1:3]) #will grab everything up to index 3 except for index 3 (Racheal and Elizabeth)

''' list functions ''' #most important structure to store information
# lucky_numbers = [42, 8, 15, 16, 23]
# friends = ["Mahlet", "Racheal", "Elizabeth", "Fahad", "Lydia"] #stores multiple values inside the same object. We can change one to a number or a Boolean and it won't matter.
# friends.extended(lucky_numbers) #puts the lists together (adding two lists together)
# friends.append("Creed") #allows us to add another element to the end of the list
# friends.insert(1,"Johnesha") #Will insert Johnesha in index position 1 and will push everything to the right one index position
# friends.remove("Creed") #Now when we run the program Creed is removed from the list
# friends.clear() #Gives us an empty lists. Removes everything in the list
# friends.pop() #removes the last element in the list
# friends.index("Mahlet") #will tell me the index of Mahlet. If I put down Mike it will say mike is not on the list
# friends.count("Mahlet") #tells us how many times we get the value Mahlet
# friends.sort() #allows us to sort the list in ascending order. Will put it in alphabetical order
# lucky_numbers.sort() #Will put numbers in ascending order as well.
# lucky_numbers.reverse() #Will give us the list backwords (23, 16, 15, 8, 42)
# friends2 = friends.copy() #Will have all the same attribute as friends.
# print(friends)

'''Tuples''' #a structure where we can store multiple pieces of information.
# coordinates = (4, 5) #use open and close paranthesis whenever we want to create a tuple. immutable: cannot be changed or modified once we create it
# #we can't change or add or erase ANYTHING. #indexed starting at zero. We cannot set it equal to anything else.
# print(coordinates[0]) #prints out 4
# #We can create a list of tuples
# coordinates = [(4, 5), (6, 7), (80, 34)] #tuples are more of a niche but if you want to store data that can't be change use a tuple


'''Functions'''#Collection of code that has a task. When we want it to do something we just call the function
# def sayhi(): #We need it to call a function (def) then we need to give the function a descriptive name
#     print("Hello user")

# sayhi() #prints Hello User (Function will not work unless we call the function again)

# def sayhi(name): #We can make functions more powerful by giving them information. Parameter is a piece of information we give to the function
#     #to specify that we need information we put 'name' in the ()
#     #whenever we call this function we have to give it a name.
#     print("Hello " + name)

# sayhi("Mike") #prints "Hello Mike"
# sayhi("Steve") #prints "Hello Steve"

# print("Top") #We want to print top
# sayhi() #We want to bring the function sayhi down here. Pythin grabs the function and executes all of the code in the function. Once it is completed
# print("Bottom") #It will print bottom after executing the function

# def sayhi(name, age): #We can add as many parameters as we want. The funcion has 2 parameteres
#     print("Hello " + name + " you are " + age)

# sayhi("Mike", "35") #prints "Hello Mike"
# sayhi("Steve", "70") #prints "Hello Steve"

# def sayhi(name, age): #You can pass any type of data into a function. If we want to insert the numbers as strings
#     print("Hello " + name + " you are " + str(age)

# sayhi("Mike", 35) #prints "Hello Mike"
# sayhi("Steve", 70) #prints "Hello Steve"
# #Great idea to break up your data 


'''Return Keyword'''
'''We call a python function we want it to execute task then give me information back. So the function can communicate back
return keyword allows python to return information from a function'''
# def cube(num): #We are going to cube the number
#     return num * num * num #nothing happens until we add return. Return: python returns whatever value you but to the right.
# print(cube(3)) #it tells us none when we input the value. #Once return is added it prints 27
'''----------------------------------------------------------------------------------------------------------'''
'''
def cube(num): #
    return num * num * num #return breaks us out of the function. Whenever it sees return it will break out of the function. 
    #We can return any data type you like
    print("code") #Any code placed after a return statement won't work. it will never print code
result = cube(4) #stores value that is returned when we execute the function. prints out 64
print(result) #
'''

'''If Functions'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#execute code when certain conditions are true. Allows our program to respond when certain inputs are given.
#When values = thing1 it does this, when value = thing2 it can do this.
# (I Wake Up)
# if I'm hungry: #This is a condition
#     I eat breakfast #If it is true i'm going to eat breakfast
#     #If it is false I am going to move on.
# (I leave my house)
# if it's cloudy:
#     I bring an umbrella #if the statement is true
# Otherwise
#     I bring sunglasses #if the statement is false
# (I'm at a restaurant)
# If I want meat #if this is true we order the steak
#     I order steak
# Otherise if I want pasta #if it is false we will check another condition. if this condition is true we get spaghetti
#     I order spaghetti & meatball
# Otherwise #if false we will just eat the salad
#     I order a salad

'''----------------------------------------------------------------------------------------------------------'''
#We want to create a Boolean variable that tells us whether or not someone is male.#must be reduced to true or false value
# is_male = False #Boolean variable. We can use an if statement to see value of variable
# if is_male: #We have to type out a true or false condition. Checking if the person is male. 
#     print("You are a male") #Will be executed while condition is true. Our condition prints out blank because it is not true.
# else: #else is otherwise 
#     print("You are female") #If it's false it will print this out. 
#     #We can put as much code as possible in an if statement

# is_male = False 
# is_tall = True

# if is_male or is_tall:  #if the person is either male or if their tall then we want to print "You are a ale or tall or both"
#     print("You are a male or tall or both")  #this says you are male or tall or both
# else:
#     print("You are neither female no tall") 


# is_male = False 
# is_tall = True

# if is_male and is_tall:  #if the person is male and is tall the bellow will print
#     print("You are a male or tall or both")  #this says you are male or tall or both
# else:
#     print("You are either not male not tall or both") #if not it will print this

'''Male and not tall'''
# elif = else if
# is_male = False 
# is_tall = True

# if is_male and is_tall:  #if the person is male and is tall the bellow will print
#     print("You are a male or tall or both")  #this says you are male or tall or both
# elif is_male and not(is_tall): #not negates whatever is inside of there
#     print("You are a short male")
# elif not(is_mail) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are either not male not tall or both") #if not it will print this

''' if statements/comparisons'''
'''comparing numbers or strings; depending on the result we can do certain things '''
# #We want to create a function that passes 3 parameters of input and prints out the biggest
# def max_num(num1, num2, num3): #specify that we want 3 numbers
#     if num1 >= num2 and num1 >= num3: #We are going to end up with a true or false value. 
#         #We are getting TorF value by using a comparison operator
#         #to find out which one of the parameters are the largest
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(mac_num(3, 4, 5)) #no matter which one is the biggest it can tell us without a problem.
# #these comparisons are the most common ways to compare using if statement
# #These are comparison operators.
# #!=


''' Building a calculator in python'''
# num1 =float(input("Enter first number")) #they have to insert a number otherwise we get an error
# qp = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/" :
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else: 
#     print("Invalid operator")



'''Dictionaries'''
'''special structure that allows us to store information in key value pairs.'''
'''word = Key
value = definition

Jan -> January
Mar -> March'''
#Creating a dictionary below (Key: Value Pairs)
# monthConversions = {
#     "Jan": "January", #Each key has to be unique or else we get a warning for duplicate keys.
#     "Feb": "February", #We can use a numbers as keys as well. They just have to unique
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",

# }
# print(monthConversions["Nov"]) #we can access the month names. Will give us back the full name for November.
# print(monthConversions.get("Dec")) #If we put LUV insteaed of Dec we get none. We should create a default value though
# print(monthConversions("Luv", "not a valid key")) #default value


'''While Loop''' #Could I place the while loop at the top of my code instead of making it completely separate for lab3.
#is basically a structure in python that allows us to loop through and go through a block of code multiple times. 
#It would execute repeatedly unless the condition was false.
'''1. create an interger'''
# i = 1
# '''create a while loop'''
# while i <= 10: #condition #condition can also be a loop guard. Keep looping through the code inside as long as this condition is true
#     #code inside while loop will repeatedly get executed as long as code is true
#     print(i)
#     i += 1 #(shorthand)
# print("Done with loop") #prints numbers 1-10 vertically

'''Building a guessing game''' #input secret word, if they do not guess it continue to ask.
# secret_word = "giraffe" #created variables
# guess = ""
# guess_count = 0 #everytime the loop goes around add 1 for the guess
# guess_limit = 3 #how many tries the user has
# out_of_guesses = False #will tell us whether or not the user is out of guesses

# while guess != secret_word and not(out_of_guesses): #as long as they haven't guessed the word or are out of guesses 
#     if guess_count < guess_limit: #if guess count is less than guess limit than they have guesses left.
#         guess = input("Enter guess: ") #if they have guesses look we ask them to enter another guess
#         guess_count += 1
#     else:
#         out_of_guesses = True #if it is equal to true then they don't get anymore guesses
# if out_of_guesses:
#     print("out of guesses, you lose!")
# else:
#     print("You win")


'''for loop in python''' #allows us to loop over different collections of items
#loop through different arrays, letters in a string, or a series of numbers.

# for letter in "Giraffe Academy" : #for every letter in giraffe academy, I want to do something
#     print(letter) #prints out Giraffe Academy vertically

# friends ["Jim", "Karen", "Kevin"]
# for friend in friends: #for each friend in this friend array, print friend. (friend) can have any random name
#     print(friend)
# friends ["Jim", "Karen", "Kevin"] #very common for looping through arrays
# len(friends) #gives us the length of the array (3, because there are 3 elements insie)
# for index in range(len(friends):
#     print(friends[index]))
#     #friends[0], friends[1], friends[2]

# for index in range(3, 10): #we can use a range to loop through an array
#     print(index) #prints out 0-10 not including 10. When we add 3, we print out the numbers between 3 and 10 not including 10

# friends = {"Jim", "Karen", "Kevin"}
# for index in range(5):
#     if index == 0:
#         print("first iteration")
#     else:
#         print("not first")


'''exponent function''' #allows us to take a certain number and raise it a certain power
# print(2**3) #2^3 power
# #How to use a for loop to create an exponent function that can do this.

# def raise_to_power(base_num, pow_num):
#     #We don't know right off the bat what the pow_num is going to be.
#     result = 1
#     for index in range(pow_num): #We will loop through as many times as Pow_num. 
#     #everytime through the loop we add one to base_num
#         result = result *base_num
#     return result
#     print(raise_to_power(3, 2))

'''2d lists & nested loops'''
# number_grid = [ #We can make everything a list 
#     [1, 2, 3], # 0#4 rows and 3 columns, allows us to create a grid like structure
#     [4, 5, 6], #row 1
#     [7, 8, 9], #row 2
#     [0] #row3
# ]
# #How to access individual values in list
# print(number_grid[0][0]) #allows us to print out just 1

# '''nested for loop'''
# for row in number_grid:
#     for col in row: #this will give us each individual item
#         print(col) #should print out every single value

#     # print(row)
'''building a translator in python'''
#take in a string and translate it into a different language.
'''
Giraffe language
vowels -> g
------------------

dog -> dgg
cat -> cgt #any value will become a g
# '''
def translate(phrase):
    translation = "" #We want to loop through every letter and if it isn't a vowel we want to leaveit alone
    for letter in phrase: #now we can access each individual letter
        if letter in "AEIOUaeiou": #checking to see if the letter is inside of this string and if it is then we know its a vowel
           #to make it more efficient we can say if letter.lower() then we only have to type out lowercase letters
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
           #It does not keep our upper case syntax
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))

'''Try/ Accept Block''' 
# # value = 10/0 #we cannot divide by zero but when we put it in the try block, it will get caught by the except and say Invalid input. (because you can't divide by zero)
# try:
#     answer =10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err: #any program that could go wrong will be excepted
#     print(err)
# except ValueError: #if we put a string instead of a number
#     print("invalid input") #depending on what happens we can do different thinks
# #ALWAYS CATCH SPECIFIC ERRORS

#We can except different types of errors

'''READING FROM EXTERNAL FILES'''
Python read command allows you to read a file that is outside of Python.
If we want to read employees from another file what we will need to do is open the file

1. open() #relative, absolute, or just the files name if both are in the same directory (folder)
2. open("employees.txt", "r") #r is a mode, r means read the file
another mode is called "w" = write
"a" = append (you can append information to the end of the file)
"r+" = read and write 
#open function just opens the file. We generally want to store it in a variable
3. employee_file = open("employees.txt")
4. employee_file.close() #how to close a file
#how to get information from a file
employee_file = open("empoyees.txt", "r")
for employee in employee_file.readlines(): #will loop through all of the employees in the employee file
    print(employee) #will print out all of the employees in that file.
employee_file.close()

print(employee_file.readable()) #returns a boolean value if we can read from the value
#if we replaced r with a w it will say no because we can only write in it.
print(employee_file.read()) #will spit out all of the information from the file. 
print(employee_file.readline()) #lets you read the individual line. Reads the first line and then moves cursor to next line
print(employee_file.readline()) #this will print the first two lines in the file.
#If we were to do this multiple times it would print out the entire file
print(employee_file.readlines()) #takes all of the lines in the file and puts them in an array.
print(employee_file.readlines()[])#to access specific line just add an index
#great way to parse through information in a file
employee_file.close() #always close files when done

'''writing to files'''
#it allows you to work with external files regardless of language.
#WE CAN ALSO WRITE A NEW FILE AND APPEND TO EXISTING FILES
employee_file = open("employees.txt", "a") #whereever the file ends we will add the text to there
employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")
#will give us a new line everytime we append.
employee_file.close()
-------------------------------------------------------
employee_file = open("employees.txt", "w") #will override the entire file and
employee_file.write("\nKelly - Customer Service")

employee_file.close() #When you look at .txt file it will add Toby
#Be very careful because you can mess up a file easily
#if we run file it will add employee again to the same line. 
#if you append something wrong to the file it is permanent.
employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()


'''modules and pip '''
#Python file that we can import into our current python file.
(#usefultoolsfile)
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename): #give it a file name and it will tell you the extension
    return filename[filename.index(.) + 1:]

def roll_dice(num):
    return random.randint(1, num)
#instead of copying and pasting this file we can import all of these functions
'''new file '''
import useful_tools #will go grab all the stuff from the file above

print(useful_tools.roll_dice(10)) #now we can access all of the attributes, when we put the cursor it should pop up
#We want to roll a ten sided dice. #We didn't have to copy anything we just imported
#Allows us to write something once and we can repeatedly use it
#Use google modules function. It's python code and variables that are already written for you
#They allow you to make your program better.
#Very is to find 3rd party modules.
#You can save a lot of time using modules
#Modules are either built-in (automatic access) or external.
#External modules are stored in the same file that we stored Python in.

#Lib = stores external modules. They are stored inside lib folder.
#source code tells you where the module is stored.
#We can install third party modules.
'''installing 3rd party modules'''
'''pythondocx = allows you to format and create google documents in python.
pip install python-docx allows you to install python docx using this program (comes pre-installed with python 3)
it is a package manager. Allows you to install and uninstall python modules.

1. open up command prompt or terminal in computer.
2. pip --version (spits out the version of pip you already have)
3. pip install python-docx (type name of python module)
#enter allows us to install everything we need for python docx.
when we install 3rd party modules it is stored in lib folder in site-packages
#if we want to use this in a program we just use docx.
'''
# import docx #Now we can do import docx at the top
# docx. #gives us all of the different modules.
# to remove:
# 1. pip uninstall python-docx
# #Pip removes modules from folder.
# 2. USE SITE-PACKAGES IN LIB FOLDER

'''classes and objects

strings: plain text
boolean values: true or false
numbers:

not all things can be represented in strings, booleans, or numbers (aka phone, computer or person)
Classes and objects allow us to create our own data types.
we can store all the information about anything.
A class says hey heres another data type that we want to use in python.
''''
#Lets say we want to model a student but we don't have a student data type
1. create new python file.
2. inside of file create student class.
    class Student: #An overview of what the student is, defines what a student is
        #everything in here is a part of our student class.
        #We can define attributes about our students
        #We can use strings, booleans and numbers.
        '''def __init__(self):''' #initialize function allows us to map out the attributes a student will have.
3.        def__init__(self, name, major, gpa, is_on_probation): #defining what a student is in our program. This is the student data type.
            self.name = name  #We can use this class inside of another file
            self.major = major #The student is storing a major is different from the one above (which are just parameters)
            self.gpa = gpa #name of students gpa is going to be equal to the gpa that we passed in.
            #self refers to the actual object 
            self.is_on_probation = is_on_probation
'''second file app.py'''#Object = an actual student with a name major and gpa (pierre)
#We want to create an actual student and give it information.
#In order to use the class we need to import it
1. from Student import Student
#first student is the file, second student is the class
#creating a class
2. student1 = Student(#name, major, gpa, and probation value)
3. student1 = student("Jim", "Business", 3.1, False) #an object is an instances of a class. (actual person)
#Above is a student object.
#takes this information and stores it as attributes.
4. print(student1) #allows us to access every attribute
print(student1.name) #prints out jim
print(student1.gpa) #prints out gpa
#create another student
5. student2 = Student("Pam", "Art", 2.5, True)
6. print(student2.gpa)


'''building a multiple-choice quiz'''
from Question import Question #we need this so it can read question
questions_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
#Above is an array with all of the question prompts that will be inside of the multiple choice quiz.
#How to represent the question is the first part.
#We need to keep track of what we want to ask, and what the answer is.
1. Create question class to store question prompt and answers.
    1. create new file
    2. create class in file:
        class Question:
            def_init_(self, prompt, answer) : #everyprompt will have a question and and an answer
                self.prompt = prompt
                self.answer = answers
3. go back to original file and create an array called questions

questions = [
    Question(question_prompts[0], "a"), #pass first question and the answer
    Question(question_prompts[1], "c"),# We created 3 questions with 3 different answers
    Question(question_prompts[2], "b"), #You can put as many questions as you want in here.

4. create a function that runs the test:
    def run_test(questions): #list of questions we want to ask
        score = 0 #everytime user answers question right we will add to the score
        for question in questions: #for each question object inside of questions we want to do something
            answer = input(question.prompt) #answer that the user entered is store in this variable
            if answer == question.answer: #is the answer the student gave = to the question we are asking
                score +=1
        print("You got " + str(score) + "/" + "correct")
run_test(questions) #Kept track of score and prints it out.
---------------------------------------------------------------------
OBJECT Function:

from Student import Student #importing from the student file and we are importing class student
student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

def on_honor_roll(self):  #Place in first file with student class
    if self.gpa >= 3.5 #checking to see if student gpa is in honor roll
        return True #What function can I put inside of here to help the user figure out information about the object
    else:
        return False 
print(student1.on_honor_roll()) #false
print(student2.on_honor_roll()) #true
-----------------------------------------------------
INHERTIANCE: where we can define attributes and functions inside of class
then create another class that inherits everything without writing the same
methods or attributes.

First file:
'''from Chef import Chef #importing the chef so we can use it'''
from ChineseChef import ChineseChef
myChef = Chef() #creating a new Chef 
myChef.make_chicken() #The chef makes a chick
myChef.make_special_dish() #makes bbq

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()

#lets create a class that modeled a Chinese Chef instead of normal chef.
#first crete a new file ChineseChef.py
1. class ChineseChef:#very specific and can do everything the other chef can do
2. #if we want to give him all of the functionality we can just copy info from previous file
class ChineseChef:
     def make_chicken(self): #the problem is we had to copy and paste the physical file
        print("The chef makes a chicken")
    def make_salad(self):
        print("The chef makes salad")
    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_fried_rice(self):
        print("the chef makes fried rice")
    #instead of copying and pasting we can inherit it 
from Chef import Chef (chef.py folder)
class ChineseChef(Chef): #inside of this Chinese chef I want to use the function in the Chef file
    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_fried_rice(self):
        print("The chef makes fried rice")

 different file (Chef.py)
class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")
    def make_salad(self):
        print("The chef makes salad")
    def make_special_dish(self):
        print("The chef makes bbq ribs")
    
-------------------------------------------------------------------
PYTHON INTERPRETER  : ALLOWS us to try and test out different Python functions.
1. open up cmder
2.Type python3 (macbook), py (windows) (how to add python 3 to windows path variable)
    hit enter
3. print("Hello World")
Hello World.
num1 = 10
num2 = 90
print(num1 + num2)
prints 100 for use

def sa_hi(name):
    print("Hello" + name);
...
...
say_hi("Mike")
Hello Mike
#not intuitive for creating a program, just use this to test: no need to set up or save a file
texteditor = better for writing a program and does not let you get confused.
