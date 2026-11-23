age = int(input('Enter your age: '))
legal_age_to_drive = 18
my_age = 31
if (age >= legal_age_to_drive):
    print('You are old enough to drive.')
else:
    print(f'You need {legal_age_to_drive-age} more years to learn to drive.')

if (age < my_age):
    if (my_age-age == 1):
        print('You are 1 year younger than me')
    else:
        print(f'You are {my_age-age} years younger than me')
elif (age > my_age):
    if (age-my_age == 1):
        print('You are 1 year older than me')
    else:
        print(f'You are {age-my_age} years older than me')
else:
    print('We are the same age!')

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if (a>b):
    print(f'{a} is greater than {b}')
elif (b>a):
    print(f'{b} is greater than {a}')
else:
    print(f'{a} and {b} are equal')

score = int(input("What is the students grade: "))

if score >= 90:
    print("A")
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

month = input("What month is it? ").lower()
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
autumn = ['september', 'october', 'november']

if month in winter:
    print('Winter')
elif month in spring:
    print('Spring')
elif month in summer:
    print('Summer')
elif month in autumn:
    print('Autumn')
else:
    print('Month Not Found')

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input("Enter new fruit: ")
if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)

person = {
    "first_name": "Marques",
    "last_name": "Robinson",
    "gender": "male",
    "age": 31,
    "marital_status": False,
    "skills": ["HTML", "CSS", "WordPress", "JavaScript", "Python", "MySQL", "AWS"],
    "country": "United States of America",
    "city": "Everett",
    "address": {
        "street": "100 Baker St",
        "zipcode": "54321"
    }
}