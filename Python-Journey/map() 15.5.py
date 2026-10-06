celsius = [30, 70, 100, 120]
fahrenheit = list(
    map
    (lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)