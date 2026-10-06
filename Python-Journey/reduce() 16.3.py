from functools import reduce
num = [23, 45, 67, 89, 12]
max_result = reduce(lambda x, y: x if x > y else y, num)
print(max_result)