is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
num = int(input("Enter a number: "))
print(f"The number {num} is {is_even(num)}.")