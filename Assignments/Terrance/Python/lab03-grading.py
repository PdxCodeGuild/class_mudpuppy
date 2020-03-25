#lab03-grading.py

user_grade = int(input("What is your grade? "))
if user_grade > 100:
    print("Good job, you got an A+!")
elif user_grade <= 100 and user_grade >= 90:
    print("Good job, you got an A.")
elif user_grade <= 90 and user_grade >= 80:
    print("Not bad, you got an B.")
elif user_grade <= 80 and user_grade >= 70:
    print("That's average, you got an C.")
elif user_grade <= 70 and user_grade >= 60:
    print("Not very good, you got an D.")
else:
    print("You failed!")