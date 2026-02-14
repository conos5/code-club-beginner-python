# === LESSON 2: NUMBERS AND MATHS ===
# Python can do maths! But there's one trick to learn first.

# When we use input(), Python thinks EVERYTHING is text
# We need int() to turn text into a number
num1 = int(input("Pick a number: "))
num2 = int(input("Pick another number: "))

# Now we can do maths with them
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} x {num2} = {num1 * num2}")


# === YOUR TURN ===
# 1. Add a line that prints the two numbers divided (use /)
# 2. Ask for a third number and print all three added together
