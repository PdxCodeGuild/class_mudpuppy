# 1. what are functions?

# Functions are a way for us to refer to a computation in an abstract and reusable way

# Abstraction - internal details can be hidden, external interface is emphasized

# Reuse - having a function allows the same computation to be executed in multiple places and contexts




# 2. examples of functions we have seen

# examples would be print(), input(), int(), float(), range(), etc.

# Cosider the abstraction principle. We don't know the internal details of how these functions are implemented.
# That's ok, as long as we understand their interface (how to use them).

# Consider the reuse principle. We can reuse these functions over and over again in many different contexts.




# 3. how to define our own functions

def add(a, b):
    return a + b





# 4. return values and arguments

# functions take in values as arguments (parameters), and return a value as a result

# Not all functions need to take in an argument, and not all functions need to return a result




# 5. formal parameters vs. actual parameters

# The abstract arguments that serve as placeholders for real values are referred to as "formal parameters".

# The real values that actually get passed into the function are referred to as "actual parameters".

def say_hello(name):
    print(f"hello {name}")

# the variable "name" is a formal parameters

say_hello('bob')

# the value 'bob' is an actual parameter




# 6. variable scope

# variables defined inside of a function only exist inside of that function

# variables defined outside of a function DO exist inside of the function

name = 'Joe'

def say_hello_2():
    print(f'hello {name}')

# notice how we can refer to name even though it was defined outside of the function

say_hello_2()

# but what if we try to refer to a variable defined inside of a function?


def my_function():
    number = 3


my_function()

print(number) # this will cause an error. number is not defined in this scope. number is only defined inside the scope of the function.