# Creating a set
numbers = {1, 2, 3, 4, 5}

# Adding an item
numbers.add(6)
print(f"Set after adding 6: {numbers}")

# Removing an item
numbers.remove(3)
print(f"Set after removing 3: {numbers}")

# Sets do not allow duplicate items
numbers.add(2)  # This won't change the set as 2 is already present
print(f"Set after attempting to add 2 again: {numbers}")

# Iterating through a set
for number in numbers:
    print(number)

# Set operations
odd_numbers = {1, 3, 5, 7}
print(f"Union: {numbers.union(odd_numbers)}")
print(f"Intersection: {numbers.intersection(odd_numbers)}")
print(f"Difference: {numbers.difference(odd_numbers)}")
