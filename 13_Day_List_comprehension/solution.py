numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([i for i in numbers if i <= 0])

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([i for items in list_of_lists for i in items])

print([(i*1, 1, i*1, i**2, i**3, i**4, i**5) for i in range(11)])