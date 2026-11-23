age = int(input('Enter your age: '))
legal_age_to_drive = 18
if (age >= legal_age_to_drive):
    print('You are old enough to drive.')
else:
    print(f'You need {legal_age_to_drive-age} more years to learn to drive.')