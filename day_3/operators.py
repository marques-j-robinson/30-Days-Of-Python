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