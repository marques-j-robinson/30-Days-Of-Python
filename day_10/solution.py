for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i+=1

for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i-=1

for i in range(7):
    print('#'*(i+1))

for i in range(8):
    s = ''
    for j in range(8):
        s += '# '
    print(s.strip())

for i in range(11):
    print(f"{i} x {i} = {i*i}")

tech = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in tech:
    print(i)

for i in range(1, 101):
    if (i % 2 == 0):
        print(i)

for i in range(1, 101):
    if (i%2!=0):
        print(i)

total = 0
even_sum = 0
odd_sum = 0
for i in range(1, 101):
    total+=i
    if(i%2==0):
        even_sum+=i
    if(i%2!=0):
        odd_sum+=i
print(f'The sum of all numbers is {total}')
print(f'The sum of all evens is {even_sum}')
print(f'The sum of all odds is {odd_sum}')

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from data.countries import countries

contries_with_land_in_name = []
for i in countries:
    if 'land' in i:
        contries_with_land_in_name.append(i)
print(contries_with_land_in_name)

fruit = ['banana', 'orange', 'mango', 'lemon']
reversed_fruit = []
for i in range(len(fruit) - 1, -1, -1):
    reversed_fruit.append(fruit[i])
print(reversed_fruit)

from data.countries_data import countries

unique_languages = set()
languages = {}
for c in countries:
    for language in c['languages']:
        unique_languages.add(language)
        if language not in languages.keys():
            languages[language] = 1
        else:
            languages[language] += 1
print(f'Total number of languages: {len(unique_languages)}')
sorted_languages = sorted(languages.items(), key=lambda item: item[1], reverse=True)
print(dict(sorted_languages[:10]))