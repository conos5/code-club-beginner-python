# === LESSON 3: MAKING DECISIONS ===
# We can make Python choose what to do using if/elif/else

# Ask the user's age and convert to a number
age = int(input("How old are you? "))

# 'if' checks a condition — is it true or false?
if age >= 13:
    print("You're a teenager!")
elif age >= 10:
    print("You're almost a teenager!")
else:
    print("You're still a kid!")

# We can also check text
password = input("What's the secret password? ")

if password == "python":
    print("Correct! You're in!")
else:
    print("Wrong password!")


# === YOUR TURN ===
# 1. Change the password to something else
# 2. Add another if/elif/else that asks for a number
#    and prints "too high", "too low", or "just right"
#    (pick any number as the correct answer)
