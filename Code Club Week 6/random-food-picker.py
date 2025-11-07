import random

print("=== RANDOM FOOD PICKER ===")

foods = ["pizza", "tacos", "sushi", "pasta", "burger", "salad"]

print("Foods available:")
print(foods)

choice_number = random.randint(0,5)
choice = foods[choice_number]

# choice = random.choice(foods) # alternate way to do it
print(f"\nYou should eat: {choice}")

print(f"Number of foods: {len(foods)}") # len means length, how many things are in list
foods.pop(2) # Remove 3rd item (index 2) of list
print(foods)

foods.append("pasta") # adds to end of list
print(foods)

foods.insert(3, "pancakes") # adds to a chosen place in the list
print(foods)


## While loops with lists
count = 0
while count < len(foods):
    print(f"Item {count} in foods list is {foods[count]}")
    count = count + 1