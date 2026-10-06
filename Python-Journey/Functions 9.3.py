def fun(evenOdd):
    if evenOdd % 2 == 0:
        print('Even')
    else:
        print('Odd')
print('Enter a number:')
num = int(input())
fun(num)