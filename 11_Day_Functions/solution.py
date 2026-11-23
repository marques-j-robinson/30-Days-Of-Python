def add_two_numbers(a, b):
    return a+b

def area_of_circle(r):
    return 3.14*r**2

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) != int:
            total = "Error: input must be integers"
            break
        total += num
    return total

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def check_season(m):
    month = m.lower()
    winter = ['december', 'january', 'february']
    spring = ['march', 'april', 'may']
    summer = ['june', 'july', 'august']
    autumn = ['september', 'october', 'november']
    if month in winter:
        return 'Winter'
    elif month in spring:
        return 'Spring'
    elif month in summer:
        return 'Summer'
    elif month in autumn:
        return 'Autumn'
    else:
        return 'Not a valid month'

def calculate_slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:
        raise ValueError('Slope is undefined (vertical line)')
    return (y2 - y1) / (x2 - x1)

import cmath
def solve_quadratic_eqn(a, b, c):
    # Check if it is a valid quadratic equation
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero.")
        
    # Calculate the discriminant (b² - 4ac)
    discriminant = (b ** 2) - (4 * a * c)
    
    # Calculate the two roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return root1, root2

def print_list(items):
    for i in items:
        print(i)

def reverse_list(items):
    result = []
    for i in range(len(items)-1, -1, -1):
        result.append(items[i])
    print(result)

def capitalize_list_items(items):
    result = []
    for i in items:
        result.append(i.capitalize())
    return result

def add_item(items, item_to_add):
    items.append(item_to_add)

def remove_item(items, item_to_remove):
    items.remove(item_to_remove)

def sum_of_numbers(num):
    total = 0
    for i in range(1, num+1):
        total+=i
    return total

def sum_of_odds(num):
    total = 0
    for i in range(1, num+1):
        if(i%2!=0):
            total+=i
    return total

def sum_of_evens(num):
    total = 0
    for i in range(1, num+1):
        if(i%2==0):
            total+=i
    return total

def evens_and_odds(num):
    if num <= 0:
        return "Must pass a positive number to this function"
    even = 0
    odd = 0
    for i in range(0, num+1):
        if(i%2==0):
            even+=1
        if(i%2!=0):
            odd+=1
    return f"The number of odds are {odd}\nThe number of evens are {even}"

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_empty(item):
    if type(item) == str:
        return item == ""
    elif type(item) == int:
        return item == 0
    elif type(item) == float:
        return item == 0.0
    elif type(item) == list or type(item) == tuple or type(item) == set or type(item) == dict:
        return len(item) == 0
    else:
        return item == None

import statistics

def calculate_mean(nums):
    return statistics.mean(nums)

def calculate_median(nums):
    return statistics.median(nums)

def calculate_mode(nums):
    return statistics.mode(nums)

def calculate_range(nums):
    return max(nums) - min(nums)

def calculate_variance(nums):
    return statistics.variance(nums)

def calculate_variance(nums):
    return statistics.stdev(nums)

def greet(name='Guest'):
    print(f'Hello, {name}!')

greet()
greet('Alice')

def show_args(**args):
    print(args)

show_args(name='test', year=2026, season='Winter')

import math
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n%i==0:
            return False
    return True
print(is_prime(11))
print(is_prime(15))

def is_unique(items):
    result = True
    for idx, i in enumerate(items):
        if i in items[idx+1:]:
            result = False
    return result

print(is_unique(['one', 'one', 'three']))

def is_datatype_unique(items):
    datatypes = set()
    for i in items:
        datatypes.add(type(i))
    return len(datatypes) == 1

print(is_datatype_unique([1, 2, 3]))
print(is_datatype_unique(['one', 'two', 'three']))
print(is_datatype_unique([1, 'two', 'three']))

import keyword
def is_valid_variable_name(name):
    return name.isidentifier() and not keyword.iskeyword(name)

print(is_valid_variable_name("my_var"))
print(is_valid_variable_name("2nd_var"))
print(is_valid_variable_name("for"))

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from data.countries_data import countries

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