from functools import reduce
s = ["Python", "Java", "C++", "JavaScript"]
sentence = reduce(lambda x, y: x + " " + y, s)
print(sentence)