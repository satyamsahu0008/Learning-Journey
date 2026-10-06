a = "Global Variable"
def fun():
    a = "Local Variable"
    print(a)
fun()
print(a)