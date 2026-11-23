empty = []
states = ['Texas', 'Washington', 'Oregon', 'Virginia', 'Colorado', 'Kansas']

print(len(states))

print(states[0])
print(states[len(states)//2])
print(states[len(states)-1])

mixed_data_types = ['Marques Robinson', 31, 5.11, False, '100 Baker St']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))

print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[len(it_companies)-1])

it_companies[0] = it_companies[0].upper()
print(it_companies)

it_companies.append('SpaceX')
print(it_companies)

mid = len(it_companies) // 2
it_companies.insert(mid, 'Tesla')
print(it_companies)

it_companies[1] = it_companies[1].upper()

print('#; '.join(it_companies))

print('Apple' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[3:])
print(it_companies[:len(it_companies)-3])

mid = len(it_companies) // 2
print(it_companies[:mid] + it_companies[mid+1:])

it_companies.pop(0)
print(it_companies)

mid = len(it_companies)//2
del it_companies[mid]
print(it_companies)

del it_companies[len(it_companies)-1]

it_companies = []

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
a = front_end+back_end
print(a)
full_stack = a.copy()
full_stack.append('Python')
full_stack.append('Redux')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = ages[0]
max_age = ages[len(ages)-1]
print(f'min: {min_age}')
print(f'max: {max_age}')

ages.append(min_age)
ages.append(max_age)

ages.sort()
mid = len(ages)//2
print(ages[mid])

print(sum(ages)/len(ages))

min_age = ages[0]
max_age = ages[len(ages)-1]
print(max_age - min_age)

avg = sum(ages)/len(ages)
print(abs((min_age-avg)-(max_age-avg)))

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from data.countries import countries
print(countries[len(countries)//2])

mid = len(countries)//2
first_half = countries[:mid+1]
second_half = countries[mid+1:]
print(len(first_half))
print(len(second_half))
