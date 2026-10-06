#Explain the difference between the Base Case and the Recursive Case with your own example.

# The base case is the condition under which the recursion stops, 
# while the recursive case is the part of the function that calls itself with a modified argument.

#example:
def factorial(n):
    if n == 0:  # Base Case
        return 1
    else:  # Recursive Case
        return n * factorial(n - 1)
print(factorial(5))