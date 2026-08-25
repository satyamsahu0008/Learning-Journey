#Swap two numbers
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

a = a + b
b = a - b
a = a - b

print("After Swapping:")
print("First Swap number:", a)
print("Second swap number:", b)