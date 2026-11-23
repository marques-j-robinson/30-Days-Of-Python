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