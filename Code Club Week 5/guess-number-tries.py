import random

secret_number = random.randint(1, 10)
guess = 0
tries = 0  # Count attempts

while guess != secret_number:
    guess = int(input("Make a guess: "))
    tries = tries + 1
    
    if guess == secret_number:
        print("🎯 Perfect! You got it!")
    elif guess < secret_number:
        print("📈 Too low!")
    else:
        print("📉 Too high!")
    
print(f"You won in {tries} tries!")
