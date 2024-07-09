# Creating a dictionary
person = {
    "name": "vijay",
    "age": 19,
    "city": "Dwarka"
}

# Accessing dictionary items
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

# Adding a new item
person["email"] = "john@example.com"
print(f"Updated dictionary: {person}")

# Removing an item
person.pop("age")
print(f"Dictionary after removing age: {person}")

# Iterating through dictionary items
for key, value in person.items():
    print(f"{key}: {value}")
