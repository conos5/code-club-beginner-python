# The Times Table Helper

# 1. Ask which times table to show
print("--- TIMES TABLE HELPER ---")
number = int(input("Which times table do you want to see? "))

# 2. Print a header
print(f"\nHere is the {number} times table:\n")

# 3. Use a for loop to print 1 to 10
i = 1
while i < 11:
    result = number * i
    print(f"{number} x {i} = {result}")
    i += 1

# Can introduce them here to for loops with range

# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")
