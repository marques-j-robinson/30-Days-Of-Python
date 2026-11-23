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