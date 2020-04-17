'''
We have to tell python how to work with our data.

Concurrency = 

How to work with classes that alread exist,
we just need to know how to work with them an how to manipulate them
to do what we want.

Composition and Inheritance:
Inheritance does lead to some problems, we won't be using composition
only inheritance.

'''
class Person:
    def __init__(self, name, age, address):
        #self is a required first argument  of any method
        #we don't have to call it self but it has to be the same
        #in every method that we use.
        self.name = name
        self.age = age
        self.address = address

    def get_name(self): #called stubbing, writing what we need but we don't know it yet
        pass #pass tells python to leave it alone and treat it as its ok
        return f'my name is  {self.name}.  I live at {self.address[0]}, {self.address[1]}, {self.address[2]}'
        #add the address 
    def get_age(self):
        pass
        return f' I am {self.age} years old'
    def get_address(self):
        pass
    return f' I live at {self.address[0]}, {self.address[1]}, {self.address[2]}'

    
    
class Employee(Person): #will inherit from person, creating another class that has access to all of the methods and functions in the Person class.
    #have access to get address, get name, and the initializer
    #when inheriting from a class with an initializer we have to call that function
    def __init__(self, name, address, occupation, department, salary):
        Person.__init__(self, name, age, adress)
        self.occupation = occupation
        self.department = department
        self.salary = salary
    
    def give_raise(self, percentage):
        self.salary = self.salary = self.salary = percentage

    
    
    
    
    
    
    person1 = Person('finn', 12, ('the treehouse', 'the land of oo', 'somewhere'))
    person2 = Persn('pepbut', 999, ('bubblegum castle', 'the land of oo', 'somewhere'))
    



    print(person1)
    print(person1.get_name())
    #print(Person.get_name(person1)) #also prints out the same thing as the above
    print(person1.get_age())
    print(person1.get_address())



    print(person2)
    print(person2.get_name())
    print(person2.get_age())
    print(person2.get_address())

    #methods are functions in a class, they are associated with the class
    #sub-routine, procedure, and functions all mean the same thing.
    #methds are only associate with classes


#private and public interfaces : some only your code can use and some only the user can.
#if someone has to look at your code you have done object oriented programming wrong.
#seperate implementation from functionality

class Employee(Person): #tells us which class we need to inherit from
    def __init__(self, age, name, occupation, salary):
        #called a child class (Person) is adult class
        #because we are inheriting from another class we have to pass a constructor
        Person.__init__(self, age, name)
        self.ccupation = occupation
        self.salary = salary
    # employee1 = Employee(54, "bruce", "salesclerk", 24500)

    def get_raise(self, amount):
        self.salary = self.salary + (self.salary * amount)
        return self.salary

employee1 = Employee(54, "bruce", "salesclerk", 24500)
print(employee1.get_name())
print(employee1.get_age())

print(employee1.give_raise(0. 10))

#composition has this class
# is a 
