class Cat:
    def __init__(self):
        self.eyes = 1
        self.color = 'orange'
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


