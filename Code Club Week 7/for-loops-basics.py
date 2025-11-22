# FOR LOOP BASICS - Introduction to for loops

print("=== FOR LOOPS BASICS ===\n")

# Comparison: While loop vs For loop
print("=== COMPARISON ===\n")

fruits = ["apple", "banana", "orange"]

# The HARD way with while loop
print("Using WHILE loop (hard way):")
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1
print()

# The EASY way with for loop
print("Using FOR loop (easy way):")
for fruit in fruits:
    print(fruit)

# Example 1: Loop through a list
print("Example 1: Printing colors")
colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(color)
print()

# Example 2: Loop through a string (strings are like lists of letters!)
print("Example 2: Printing each letter in a word")
word = "cat"

for letter in word:
    print(letter)
print()

# Example 3: Using the item in operations
print("Example 3: Doubling numbers")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    doubled = num * 2
    print(f"{num} doubled is {doubled}")
print()

# Example 4: With f-strings
print("Example 4: Greeting people")
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(f"Hello, {name}!")
print()
