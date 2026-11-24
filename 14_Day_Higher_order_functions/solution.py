# Map is a built in function that takes a function and iterable as parameters
# map(function, iterable)

# The filter() function calls the specified function which returns boolean for
# each item of the specified iterable (list). It filters the items that satisfy
# the filtering criteria.
# filter(function, iterable)

# The reduce() function is defined in the functools module and we should import
# it from this module. Like map and filter it takes two parameters, a function
# and an iterable. However, it does not return another iterable, instead it
# returns a single value.
# numbers_str = ['1', '2', '3', '4', '5']  # iterable
# def add_two_nums(x, y):
#     return int(x) + int(y)

# total = reduce(add_two_nums, numbers_str)
# print(total)    # 15