import random

secret_number = random.randint(1, 10)
guess = 0
while guess != secret_number:
    guess = int(input("Guess my number (1-10): "))

    if guess == secret_number:
        print("🎯 Perfect! You got it!")
    elif guess < secret_number:
        print("📈 Too low!")
    else:
        print("📉 Too high!")
    
print(f"Good job! The secret number was {secret_number}")
