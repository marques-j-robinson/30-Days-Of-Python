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

def square(n):
    return n**2
squared_numbers = map(square, numbers)
print(list(squared_numbers))

new_names = map(uppercase, names)
print(list(new_names))

def no_land(x):
    return 'land' not in x
new_countries = filter(no_land, countries)
print(list(new_countries))

def no_six_chars(x):
    return len(x) != 6
new_countries = filter(no_six_chars, countries)
print(list(new_countries))

def more_than_six_chars(x):
    return len(x) <= 6
new_countries = filter(more_than_six_chars, countries)
print(list(new_countries))

def start_without_E(x):
    return x[0] != 'E'
new_countries = filter(start_without_E, countries)
print(list(new_countries))

from functools import reduce

def is_even(n):
    return n%2==0
def add_two_nums(a, b):
    return a+b
new_numbers = reduce(add_two_nums, filter(is_even, map(square, numbers)))
print(new_numbers)

def get_string_lists(items):
    return list(map(lambda i: str(i), items))
print(get_string_lists(numbers))

total = reduce(add_two_nums, numbers)
print(total)

def concat_str(a, b):
    if b != 'Iceland':
        return f'{a}, {b}'
    else:
        return f'{a}, and {b} are north European countries'
concat_countries = reduce(concat_str, countries)
print(f"{concat_countries}")

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from data.countries import countries
def categorize_countries(pattern):
    def ends_with(c):
        return c.find(pattern) != -1
    return list(map(lambda i: i.title(), filter(ends_with, map(lambda i: i.lower(), countries))))

print(categorize_countries('land'))
print(categorize_countries('ia'))
print(categorize_countries('island'))
print(categorize_countries('stan'))

def countries_dict():
    res = {}
    for c in countries:
        if c[0] not in res:
            res[c[0]] = 1
        else:
            res[c[0]] += 1
    return res

print(countries_dict())

def get_first_ten_countries():
    return countries[:10]
print(get_first_ten_countries())

def get_last_ten_countries():
    return countries[len(countries)-10:]
print(get_last_ten_countries())

from data.countries_data import countries

countries.sort(key=lambda c: c['name'])
print(list(map(lambda i: i['name'], countries)))
countries.sort(key=lambda c: c['capital'])
print(list(map(lambda i: i['capital'], countries)))
countries.sort(key=lambda c: c['population'])
print(list(map(lambda i: i['name'], countries)))

def most_spoken_languages():
    languages = {}
    for c in countries:
        for language in c['languages']:
            if language not in languages.keys():
                languages[language] = 1
            else:
                languages[language] += 1
    sorted_languages = sorted(languages.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_languages[:10])

print(most_spoken_languages())

def most_populated_countries():
    population = {}
    for c in countries:
        if c['name'] not in population:
            population[c['name']] = c['population']
    sorted_pop = sorted(population.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_pop[:10])

print(most_populated_countries())