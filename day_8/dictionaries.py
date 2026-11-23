dog = {}
dog['name'] = 'Sparky'
dog['color'] = 'black'
dog['legs'] = 4
dog['age'] = 2

print(dog)

student = {
    "first_name": "Marques",
    "last_name": "Robinson",
    "gender": "male",
    "age": 31,
    "marital_status": False,
    "skills": ["HTML", "CSS", "WordPress", "JavaScript", "Python", "MySQL", "AWS"],
    "country": "United States of America",
    "city": "Everett",
    "address": "100 Baker St"
}

print(len(student))
print(type(student['skills']), student['skills'])

student['skills'].append('C')

print(list(student.keys()))