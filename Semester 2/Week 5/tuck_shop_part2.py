# === TUCK SHOP CALCULATOR (Part 2) ===
# Now we add a LOOP so you can keep buying!

# Step 1: Create a function to show the menu
def show_menu():
    print("=== TUCK SHOP MENU ===")
    print("1. Crisps     - €1.50")
    print("2. Chocolate  - €2.00")
    print("3. Juice Box  - €1.00")
    print("4. Cookie     - €1.50")
    print("======================")

# Step 2: Create a function that RETURNS the price for an item
def get_price(item_number):
    if item_number == 1:
        return 1.50
    elif item_number == 2:
        return 2.00
    elif item_number == 3:
        return 1.00
    elif item_number == 4:
        return 1.50
    else:
        return 0

# Step 3: Create a function that checks if we can afford an item
def can_afford(price, money):
    if money >= price:
        return True
    else:
        return False


# === MAIN PROGRAM ===

# Step 4 (NEW): Ask how much money they have BEFORE the loop
money = float(input("How much money do you have? €"))

# Step 5 (NEW): Use a while loop so they can keep shopping
while True:
    show_menu()
    print(f"You have €{money} to spend.")

    # Step 6: Ask what they want and get the price
    choice = int(input("\nWhat item number do you want? "))
    price = get_price(choice)

    if price == 0:
        print("That's not on the menu!")
    else:
        print(f"That costs €{price}")

        if can_afford(price, money):
            change = round(money - price, 2)
            print(f"Here you go! Your change is €{change}")
            money = change  # Update money to the change left
        else:
            short = round(price - money, 2)
            print(f"Sorry! You need €{short} more.")

    # Step 7 (NEW): Ask if they want to keep shopping
    buy_more = input("\nDo you want to buy something else? (yes/no) ")
    if buy_more.lower() != "yes":
        print("Thank you, come again!")
        break
    else:
        print("\nLet's see the menu again!")
