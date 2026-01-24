# The Rollercoaster Gate
print("--- WELCOME TO THE SUPER ROLLERCOASTER ---" \
"\nYou must be 110cm to ride")

# 1. Get height input
height = int(input("How tall are you in cm? "))

# 2. Check conditions
if height >= 110:
    print("You're good to go!")
elif height < 50:
    print("Unfortunately you will not be secure in the seat")
else:
    remaining = 110 - height
    print(f"Sorry! You need to grow {remaining}cm more.")
