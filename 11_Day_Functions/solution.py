def add_two_numbers(a, b):
    return a+b

def area_of_circle(r):
    return 3.14*r**2

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) != int:
            total = "Error: input must be integers"
            break
        total += num
    return total