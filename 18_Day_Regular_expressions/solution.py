import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph = re.sub(r'\.', '', paragraph)

def most_common_words(input, qty):
    res = []

    for word in re.split(' ', input):
        if (not any(len(t) > 1 and t[1] == word for t in res)):
            count = len(re.findall(rf"\b{word}\b", input))
            res.append((count, word))

    res = sorted(res, key=lambda x: (x[0], x[1]), reverse=True)
    return res[:qty]

# print(f"Most common word from paragraph is: {most_common_words(paragraph, 1)[0][1]}")

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

points = sorted([int(i) for i in re.findall(r'-?\d+', text)])
# print(points[len(points)-1] - points[0])

def is_valid_variable(var):
    return re.search(r'[-\d]', var) == None

# print(is_valid_variable('first_name')) # True
# print(is_valid_variable('first-name')) # False
# print(is_valid_variable('1first_name')) # False
# print(is_valid_variable('firstname')) # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_text = re.sub(r'[\%\$\#\@\&\;\.\,\?\!]', '', sentence)

print(most_common_words(clean_text, 3))