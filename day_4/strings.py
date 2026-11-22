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

print(s.find('C'))
print(s.find('F'))

s = 'Coding For All People'
print(s.rfind('l'))

s = 'You cannot end a sentence with because because because is a conjunction'
print(s.find('because'))
print(s.rfind('because'))

s = s.replace('because because because ', '')
print(s)

s = 'You cannot end a sentence with because because because is a conjunction'
print(s.find('because'))

s = s.replace('because because because ', '')
print(s)

s = 'Coding For All'
print(s.startswith('Coding'))
print(s.endswith('coding'))

s = '   Coding For All      '
print(s.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')