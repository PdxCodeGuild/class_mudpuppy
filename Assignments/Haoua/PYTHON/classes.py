#piece of object
#incapsulation gives us the ability to allo users to interactive with the software.
#small talk is the first object oriented programming language.
#The things you create are central to your software.
#They interact with each other and other versions of each other.
#Spend a lot of time planning your class and planning how it will interactive with each other.
#We can write our own classes when we get into Django. 
class Person:
    def __init__(self, name, age, height, address): #magical function
        self.name = name1
        self.age = age
        self.height = height
        self.address = address

    def get_name(self):#sets the values, allows us to return or print the values
        return f' my name is' (self.name)

    def make_older(self):
        self.age += 1

    def shrink_because_your_old(self):
        self.height +=1

    def get_address(self):
        return f'i live at' (self.address[0]), (self.address[1]), (self.address[2])
person1 = Person(name, age, height, address) street
print(person1.get_name())
print(person1.get_address())
print(person1.age)
print(person1.make_older())


__init__ #allows us to create our own instead of its 

Person#calls the class
self #is behind the scenes, we never have to pass anything for self, we only have to take care of every argument after self
#self is passed implicitly. 
#By creating a class we create a blueprint for the rest of class.
#python passes self (it's different for each instance(object) but they are still unique.)
#we have to pass self regardless.


'''When to use a class and when not to?'''
#don't use a class unless you have to or have to share the data

class LightBulb:
    def __init__(self,state): # the constructuor
        self.state = False

    def flip_switch(self):
        self.state = not self.state
    bulb1 = LightBulb(True)
    bulb2 = LightBulb(False)
    bulb3 = LightBulb(True)

    print(bulb1.flip_switch())
    print(bulb2.flip_switch())
    print(bulb3.flip_switch())


#allows us to design software on a larger scale
#ATM lab doesn't make sense to make it a class
#Don't have the time to go through that, until we use django and everything is a class
#complex projects = classes
#TIC TAC TOE lab


