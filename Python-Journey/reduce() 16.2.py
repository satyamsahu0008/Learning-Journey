from functools import reduce
num = [2, 4, 6, 8, 10]
product_result = reduce(lambda x, y: x * y, num)
print(product_result)