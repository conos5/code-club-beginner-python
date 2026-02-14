# === LESSON 4: LOOPS ===
# Loops repeat code so we don't have to write it over and over

# A 'for' loop runs a set number of times
print("Counting to 5:")
for i in range(5):
    print(i + 1)

# We can use the loop number to do things
print("\n3 times table:")
for i in range(1, 11):
    answer = 3 * i
    print(f"3 x {i} = {answer}")

# A 'while' loop keeps going UNTIL something changes
print("\nGuess the number!")
secret = 7

guess = int(input("Your guess: "))
while guess != secret:
    print("Nope, try again!")
    guess = int(input("Your guess: "))

print("You got it!")


# === YOUR TURN ===
# 1. Change the for loop to print the 5 times table instead
# 2. Change the secret number to something else
