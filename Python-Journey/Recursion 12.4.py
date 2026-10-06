#Iteration
fact = 1
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is", fact)

#Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))