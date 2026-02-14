# === LESSON 5: LISTS ===
# A list stores multiple things in one variable

# Create a list with square brackets
foods = ["pizza", "chips", "ice cream", "pasta"]

# Print the whole list
print(f"My favourite foods: {foods}")

# Print one item — lists start counting at 0!
print(f"First food: {foods[0]}")
print(f"Second food: {foods[1]}")

# Add something to the list
new_food = input("Add a food to the list: ")
foods.append(new_food)
print(f"Updated list: {foods}")

# Loop through the list
print("\nAll my foods:")
for food in foods:
    print(f"- {food}")


# === YOUR TURN ===
# 1. Change the list to your own favourite foods
# 2. Ask the user to add TWO more foods (you'll need two inputs)
# 3. Print how many foods are in the list using len()
#    Hint: print(f"I have {len(foods)} foods")
