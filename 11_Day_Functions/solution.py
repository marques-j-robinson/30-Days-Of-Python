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