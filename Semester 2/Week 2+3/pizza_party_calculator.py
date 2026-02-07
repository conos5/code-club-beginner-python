# Pizza Party Calculator

# 1. Ask how many friends are coming
print("--- PIZZA PARTY CALCULATOR ---")
friends = int(input("How many friends are coming to the party? "))

# 2. Ask how many slices each person wants
slices_per_person = int(input("How many slices does each person want? "))

# 3. Calculate total slices needed
total_slices = friends * slices_per_person
print(f"\nYou need {total_slices} slices total.")

# 4. Calculate pizzas needed (8 slices per pizza)
pizzas_needed = total_slices / 8

# 5. Round up if needed
if pizzas_needed % 1 != 0:
    pizzas_needed = int(pizzas_needed) + 1
else:
    pizzas_needed = int(pizzas_needed)

print(f"You should order {pizzas_needed} pizzas!")

# 6. Calculate leftover slices
leftover = (pizzas_needed * 8) - total_slices
if leftover > 0:
    print(f"You'll have {leftover} slices left over for later!")
else:
    print("Perfect! No leftovers.")
