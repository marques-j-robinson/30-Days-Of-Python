# Map is a built in function that takes a function and iterable as parameters
# map(function, iterable)

# The filter() function calls the specified function which returns boolean for
# each item of the specified iterable (list). It filters the items that satisfy
# the filtering criteria.
# filter(function, iterable)

# The reduce() function is defined in the functools module and we should import
# it from this module. Like map and filter it takes two parameters, a function
# and an iterable. However, it does not return another iterable, instead it
# returns a single value.
# numbers_str = ['1', '2', '3', '4', '5']  # iterable
# def add_two_nums(x, y):
#     return int(x) + int(y)

# total = reduce(add_two_nums, numbers_str)
# print(total)    # 15

# Higher order functions basically represents what all a function can do and in
# python it is pretty much everything. Python treats functions as higher order objects.
# Allowing them to take one or more functions as parameters, be returned as the result of another function,
# be modified, and be assigned to variables.

# Closure
# Python allows a nested function to access the outer scope of the enclosing function.
# In Python, closure is created by nesting a function inside another encapsulating
# function and then returning the inner function. 

# Decorators
# A decorator is a design pattern in Python that allows a user to add new functionality
# to an existing object without modifying its structure.

# This is a function that is passed in as an argument to the higher order function and will be executed for each
# item in the iterable sequence also passed in to map, filter, or reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

for i in countries:
    print(i)

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for i in names:
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i)

def uppercase(x):
    return x.upper()
new_countries = map(uppercase, countries)
print(list(new_countries))