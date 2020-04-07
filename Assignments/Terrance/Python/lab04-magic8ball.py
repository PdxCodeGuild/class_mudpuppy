print("Hey! Try my new magic8ball.")
#module
import random

### variables
# a list of magic 8 ball possible answers
magic8ball_answers =["it is certain", "as I see it", "most likely", "outlook good", "signs point to yes"]

# user greeting

user_question = input ("Ask it a question")

user_answer = random.choice(magic8ball_answers)

# f string - way more efficient
print(f"Your random answer is {user_answer}!")
