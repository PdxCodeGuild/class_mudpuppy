#Test Examples, May 6th, 2020

class Frenchie:
    def __init__(self, color='lilac fawn', eyes=2, legs=4, hunger=10):
        self.color = color
        self.eyes = eyes
        self.legs = legs
        self.hunger = hunger
    
    def eat(self):
        self.hunger -= 3
        if self.hunger < -2:
            print('This is a sick puppy')

class StopEatingMixin:
    def eat(self):
        if self.hunger <= 0:
            print('The dog isn\'t hungry')
        else:
            super().eat()

class SmartFrenchie(StopEatingMixin, Frenchie):
    pass

Cuvee = SmartFrenchie(color='gray')
Cuvee.eat()
Cuvee.eat()
Cuvee.eat()
Cuvee.eat()
Cuvee.eat()

for i in range(10):
    Cuvee.eat()
