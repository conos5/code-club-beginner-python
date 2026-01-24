import random

secret_number = random.randint(1, 10)
guess = int(input("Guess my number (1-10): "))

if guess == secret_number:
    print("🎯 Perfect! You got it!")
elif guess < secret_number:
    print("📈 Too low!")
else:
    print("📉 Too high!")
    
print(f"The secret number was {secret_number}")
