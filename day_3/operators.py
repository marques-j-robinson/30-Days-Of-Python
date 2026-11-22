age = 31
print(age, type(age))
height = 5.11
print(height, type(height))
x = 4-4j
print(x, type(x))

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = 0.5*base*height
print(f'The area of the triangle is {area_of_triangle}')

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter_of_triangle = a+b+c
print(f'The perimeter of the triangle is {perimeter_of_triangle}')

length = int(input("Enger length: "))
width = int(input("Enger width: "))
area_of_rectangle = length*width
print(f'The area of the rectangle if {area_of_rectangle}')
perimeter_of_rectangle = 2*(length+width)
print(f'The perimeter of the rectangle if {perimeter_of_rectangle}')

radius = int(input("Enter radius: "))
area_of_circle = 3.14*radius*radius
print(f'The area of the circle is {area_of_circle}')
circum_of_cirlce = 2 * 3.14 * radius
print(f'The circumference of the cirlce is {circum_of_cirlce}')

# Equation: y = mx + b
m = 2
b = -2

slope_a = m
y_intercept = b
x_intercept = -b / m # Solving 0 = mx + b for x

print(f"Slope: {slope_a}")
print(f"x-intercept: ({x_intercept}, 0)")
print(f"y-intercept: (0, {y_intercept})")


x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2-y1)/(x2-x1)
print(f'Slope: {slope}')
euclidean_distance= ((x2-x1)**2+(y2-y1**2)**0.5)
print(f'Euclidean distance: {euclidean_distance}')

slope_diff = abs(slope_a - slope)
print(f'Difference between slopes: {slope_diff}')

x = -3
y = x**2 + 6*x + 9
print(y)

len_str_one = len('python')
len_str_two = len('dragon')
print(len_str_one != len_str_two)
print('on' in 'python' and 'on' in 'dragon')

sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)

print('on' not in 'python' and 'on' not in 'dragon')

s = 'python'
s_len = len(s)
print(f"The length of string 'python' is {s_len} {type(s_len)}")
s_len_float = float(s_len)
print(f"The float value for the length is {s_len_float} {type(s_len_float)}")
s_len_float_str = str(s_len_float)
print(f"The string value of the float length is {s_len_float_str} {type(s_len_float_str)}")

n = 1
print(f'Is {n} even? {n%2==0}')
n = 2
print(f'Is {n} even? {n%2==0}')
n = 1
print(f'Is {n} odd? {n%2!=0}')
n = 2
print(f'Is {n} odd? {n%2!=0}')

floor_division = 7//3
print(floor_division == int(2.7))