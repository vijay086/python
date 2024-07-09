# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing list items
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Third fruit: {fruits[2]}")

# Adding an item
fruits.append("orange")
print(f"List after adding orange: {fruits}")

# Removing an item
fruits.remove("banana")
print(f"List after removing banana: {fruits}")

# Iterating through a list
for fruit in fruits:
    print(fruit)

# Slicing a list
print(f"Sliced list (first two fruits): {fruits[:2]}")
