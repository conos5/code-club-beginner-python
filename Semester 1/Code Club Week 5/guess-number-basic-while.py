import random

secret_number = random.randint(1, 10)
guess = 0

print("=== NUMBER GUESSING GAME ===")
print("I'm thinking of a number between 1 and 10...")

while guess != secret_number:
    guess = int(input("Make a guess: "))
    
print(f"You got it! The number was {secret_number}")
