from functools import reduce
num = [23, 45, 67, 89, 12]
sum_result = reduce(lambda x, y: x + y, num)
print(sum_result)
