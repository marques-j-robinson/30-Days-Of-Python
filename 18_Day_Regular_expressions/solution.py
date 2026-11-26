import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph = re.sub(r'\.', '', paragraph)

res = []

for word in re.split(' ', paragraph):
    print(res)
    if (not any(len(t) > 1 and t[1] == word for t in res)):
        count = len(re.findall(word, paragraph))
        res.append((count, word))

res = sorted(res, key=lambda x: x[0], reverse=True)

print(f"Most common word from paragraph is: {res[0][1]}")
