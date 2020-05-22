class Cat:
    def __init__(self, eyes, color):
        self.eyes = eyes
        self.color = color
        self.size = 'large'
        self.tiredness = 0
        self.hunger = 0
        self.favorite_food = 'lasagna'

    def sleep(self):
        self.tiredness -= 5
        if self.tiredness < 5 and self.hunger < 5:
            print('purrr')

    def eat(self, food_str=None):
        if food_str == None:
            self.hunger -= 5
        elif food_str == self.favorite_food:
            print('Thank you!')
            self.hunger -= 10
        else:
            print('No thanks')

    def wander(self):
        if self.eyes == 1:
            print('Thump!')
            self.hunger += 5
        elif self.eyes == 2:
            self.hunger += 2


my_cat = Cat(1, 'orange')
print(my_cat.tiredness, my_cat.hunger)
my_cat.wander()
my_cat.sleep()
my_cat.eat()

