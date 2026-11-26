import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph = re.sub(r'\.', '', paragraph)

res = []

for word in re.split(' ', paragraph):
    if (not any(len(t) > 1 and t[1] == word for t in res)):
        count = len(re.findall(word, paragraph))
        res.append((count, word))

res = sorted(res, key=lambda x: x[0], reverse=True)

# print(f"Most common word from paragraph is: {res[0][1]}")

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

points = sorted([int(i) for i in re.findall(r'-?\d+', text)])
print(points[len(points)-1] - points[0])