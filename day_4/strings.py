a, b, c = 'Coding', 'For', 'All'
string = f"{a} {b} {c}"
print(string)

a, b, c, d = 'Thirty', 'Days', 'Of', 'Python'
string = f"{a} {b} {c} {d}"
print(string)

company = 'Coding For All'
print(company)
print(len(company))

company = company.upper()
print(company)

company = company.lower()
print(company)

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company.partition(" ")[2])

print(company.find("Coding") >= 0)

print(company.replace('coding', 'Python'))

print('Python for Everyone'.replace('Everyone', 'All'))

print('Coding For All'.split())

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

print("Coding For All"[0])

s = "Coding For All"
print(s[len(s)-1])
print(s[10])

s = "Python For Everyone"
print("".join(word[0].upper() for word in s.split(" ")))

s = "Coding For All"
print("".join(word[0].upper() for word in s.split(" ")))