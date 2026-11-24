numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([i for i in numbers if i <= 0])

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([i for items in list_of_lists for i in items])

print([(i*1, 1, i*1, i**2, i**3, i**4, i**5) for i in range(11)])

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([[t[0].upper(), t[0][:3].upper(), t[1]] for c in countries for t in c])
print([{"country": t[0], "city": t[1]} for c in countries for t in c])

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

print([f'{n[0]} {n[1]}' for name in names for n in name])

# Calculate slope: m = (y2 - y1) / (x2 - x1)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
# Calculate y-intercept: b = y1 - m * x1
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1

# Example using points (2, 5) and (4, 9)
m = slope(2, 5, 4, 9)        # Output: 2.0
b = y_intercept(2, 5, 4, 9)  # Output: 1.0

print(m)
print(b)