def student_details(name, age, class_name, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"class_name: {class_name}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
student_details("john", 20, "12th", city="New York", country="USA")
student_details("Alice", 22, "10th", city="Los Angeles", country="USA", hobby="painting")