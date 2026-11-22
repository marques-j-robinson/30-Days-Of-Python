# Day 2: 30 Days of python programming
first_name = input("What is your first name? ") or "Marques"
print(first_name, type(first_name))
last_name = input("What is your last name? ") or "Robinson"
print(last_name, type(last_name))
full_name = f"{first_name} {last_name}"
print(full_name, type(full_name))
country = input("What country do you live in? ") or "United States of America"
print(country, type(country))
city = "Everett"
print(city, type(city))
age = int(input("How old are you? ")) or 31
print(age, type(age))
year = 2026
print(year, type(year))
is_married = False
print(is_married, type(is_married))
is_true = True
print(is_true, type(is_true))
is_light_on = True
print(is_light_on, type(is_light_on))
bg_color, highlight, shadow = 'Blue', 'Yellow', 'Brown'
print(bg_color, type(bg_color))
print(highlight, type(highlight))
print(shadow, type(shadow))

print(f'Length of first name, {len(first_name)}')
print(f'difference between first and last name: {abs(len(first_name)-len(last_name))}')

num_one = 5
num_two = 6
total = num_one+num_two
print(total)
diff = num_two-num_one
print(diff)
product = num_two*num_one
print(product)
division = num_one/num_two
print(division)
remainder = num_two%num_one
print(remainder)
exp = num_one**num_two
print(exp)
floor_division = num_one//num_two
print(floor_division)

import math

r = int(input("What is the radius of circle? "))

area_of_circle = math.pi * (r**2)
print(f'area of circle with radius {r} meters is {area_of_circle:.2f} meters')

circum_of_circle = 2 * math.pi * r
print(f'circumference of circle with radius {r} meters is {circum_of_circle:.2f} meters')

help('keywords')