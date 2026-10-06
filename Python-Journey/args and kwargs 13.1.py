def add_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(add_numbers(1, 2, 3, 4))