from functools import reduce
num = [23, 45, 67, 89, 12]
sum_result1 = reduce(lambda x, y: x + y, num)
sum_result2 = list(filter(lambda x: x > 0, [sum_result1]))
sum_result3 = list(map(lambda x: x * 2, sum_result2))
print(sum_result3)
print(sum_result1)
print(sum_result2)