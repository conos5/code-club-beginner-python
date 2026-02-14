def get_menu():
    print('''=== TUCK SHOP MENU ===
    1. Crisps     - €1.50
    2. Chocolate  - €2.00
    3. Juice Box  - €1.00
    4. Cookie     - €1.50
    ======================''')

def get_price(item_number):
    if item_number == 1:
        return 1.50
    elif item_number == 2:
        return 2
    elif item_number == 3:
        return 1
    elif item_number == 4:
        return 1.50
    else:
        print(f'There is no item {item_number}')
        return 0

def can_afford(money, item_cost):
    if money >= item_cost:
        return True
    else:
        return False
    
money = float(input("How much money do you have? "))

# Start loop here


get_menu()
# Ask user if they want to purchase an item

# if they don't, break from loop

item = int(input("What number item would you like? "))
item_cost = get_price(item)
print(f"That item is €{item_cost}")


if can_afford(money, item_cost):
    change = money - item_cost
    # Update money variable to be the change
    print(f"Here is your change €{change}")
else:
    short = item_cost - money
    print(f"You cannot afford that, you need €{short}")




