# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
it_companies.update(['SpaceX', 'Tesla'])
it_companies.remove('Twitter')
# remove() raises a KeyError if the element is not in the set, whereas discard() does nothing and raises no error.
it_companies.discard('Twitter')
it_companies.discard('Tesla')

print(A|B)
print(A&B)
print(A.issubset(B))