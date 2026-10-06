def employee_info(*args, **kwargs):
    print("Employee Information:")
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

employee_info(name="John Doe", age=30, position="Software Engineer", department="IT", location="New York")
employee_info(name="Alice Smith", age=28, position="Data Scientist", department="Data Science", location="San Francisco", hobby="painting")