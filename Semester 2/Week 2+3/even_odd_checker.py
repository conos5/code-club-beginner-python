# Even or Odd Checker
# Learn about the modulo operator (%)!

print("--- EVEN OR ODD CHECKER ---\n")

number = int(input("Enter a number: "))

# The modulo operator (%) gives us the remainder
# If a number divided by 2 has no remainder (0), it's even!
if number % 2 == 0:
    print(f"{number} is EVEN!")
else:
    print(f"{number} is ODD!")