print("=== MULTI-NUMBER CALCULATOR ===")

how_many = int(input("How many numbers do you want to add? "))

# Check if reasonable number
if how_many > 10:
    print("That's too many! Maximum is 10.")
elif how_many < 1:
    print("You need at least 1 number!")
else:
    count = 0
    total = 0
    # numbers = []
    
    while count < how_many:
        print(f"\nCurrent total: {total}")
        num = int(input(f"Enter number {count + 1}: "))
        # numbers.append(num)
        total = total + num
        count = count + 1
    
    print(f"\n🎉 Final total: {total}")
    # print(f"All numbers {numbers}")
