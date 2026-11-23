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