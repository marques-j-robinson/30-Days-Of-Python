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