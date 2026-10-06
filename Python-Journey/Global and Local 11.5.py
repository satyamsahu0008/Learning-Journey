# Explain the difference between Global and Local variables with your own example.

# Global variables are defined outside of any function and can be accessed from anywhere in the code, 
# while local variables are defined within a function and can only be accessed within that function.

#example:
a = "Global Variable"

def fun():
    a = "Local Variable"
    print(a)

fun()
print(a)