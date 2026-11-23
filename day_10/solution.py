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