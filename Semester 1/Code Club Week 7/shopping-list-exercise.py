print("=== SHOPPING LIST ===\n")

# Start with a pre-made list
shopping_list = []

print("Let's add 3 items to your shopping list!")

# Get 3 items from user
count = 1
while count <= 3:
    item = input(f"Item {count}: ")
    shopping_list.append(item)
    count = count + 1

print("\n" + "="*30)
print("YOUR SHOPPING LIST:")
print("="*30)

# Use FOR loop to print each item
item_number = 1
for item in shopping_list:
    print(f"{item_number}. {item}")
    item_number = item_number + 1

print("="*30)
print(f"\nTotal items: {len(shopping_list)}")
