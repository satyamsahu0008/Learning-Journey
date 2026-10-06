dict = {
    "student": {
        "name": "john doe",
        "age": 30,
        "city": "New York"
    }
}
dict["course"] = "Python"
print(dict["student"].update({"age": 31}))
print(dict)