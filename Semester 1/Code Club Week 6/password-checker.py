password = "python123"
guess = ""
attempts = 0

print("=== PASSWORD CHECKER ===")

while guess != password:
    guess = input("Enter the password: ")
    attempts = attempts + 1
    
    if guess == password:
        print("✅ Access granted!")
    else:
        print("❌ Wrong password! Try again.")
    
print(f"You took {attempts} attempts.")


# while guess != password and attempts < 5:

#  add attempts check
