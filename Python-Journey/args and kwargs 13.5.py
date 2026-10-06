def product_details(name, price, **kwargs):
    print(f"Product Name: {name}")
    print(f"Price: ${price}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")
product_details("Laptop", 1200, brand="Dell", model="XPS 15", warranty="2 years")
product_details("Smartphone", 800, brand="Samsung", model="Galaxy S21", warranty="1 year", color="Phantom Gray")