number = int(input("Enter a number: "))

match number:
    case 1:
        print("The number is one.")
    case 2 | 3:
        print("The number is two or three.")
    case _:
        print("The number is something else.")