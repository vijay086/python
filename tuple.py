# Creating a tuple
colors = ("red", "green", "blue")

# Accessing tuple items
print(f"First color: {colors[0]}")
print(f"Second color: {colors[1]}")
print(f"Third color: {colors[2]}")

# Tuples are immutable, so we can't change their values, but we can concatenate them
more_colors = colors + ("yellow", "purple")
print(f"Concatenated tuple: {more_colors}")

# Iterating through a tuple
for color in colors:
    print(color)
