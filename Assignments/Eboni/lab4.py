"""
Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
"""
#grades = ["A", "B", "C", "D", "F"]

num = 95

if num > 90 and num < 99:
    print("A")
elif num > 80 and num < 89:
    print ("B")
elif num > 70 and num < 79:
    print ("C")
elif num > 60 and num < 69:
    print ("D") 
elif num > 0 and num < 59:
    print ("F")






