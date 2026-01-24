print("=== SHOPPING LIST MANAGER ===")

shopping_list = []  # Start with empty list

keep_adding = "yes"

while keep_adding == "yes":
    item = input("What item do you need? ")
    shopping_list.append(item)
    
    print(f"\nCurrent list: {shopping_list}")
    print(f"Items in list: {len(shopping_list)}")
    
    keep_adding = input("\nAdd another item? (yes/no): ")

## Show the shopping list
print("\n📝 FINAL SHOPPING LIST:")
print(shopping_list)
print(f"Total items: {len(shopping_list)}")


# count = 0
# while count < len(shopping_list):
#     print(f"Item {count} in shopping list is {shopping_list[count]}")
#     count = count + 1

# Alternative way:
# for item in shopping_list:
#     print(f"{item}")
