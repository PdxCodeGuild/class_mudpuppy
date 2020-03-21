user_grade = int(input('What is your score? '))
second_digit = user_grade % 10
if second_digit < 5:
    suffix = '-'
elif second_digit > 5:
    suffix = '+'
elif second_digit == 5:
    suffix = ''
if user_grade >= 90:
    print(f"Congrats you got a A{suffix}")
elif user_grade >= 80 and user_grade < 90:
    print(f"Congrats you got a B{suffix}")
elif user_grade >= 70 and user_grade < 80:
    print(f"You\'re just an average C{suffix} student")
elif user_grade >= 60 and user_grade < 70:
    print(f"Try harder, you got a D{suffix}")
elif user_grade <= 59:
    print('You failed....')
