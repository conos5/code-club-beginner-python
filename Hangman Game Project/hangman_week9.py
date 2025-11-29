import random

print("=== HANGMAN ===\n")
print("Welcome to Hangman!")

# Game Setup

# Pick a random word
words = ["python", "code", "game", "computer", "music", "pizza", "dragon"]
secret_word = random.choice(words)
print(f"The word has {len(secret_word)} letters")

# Set up guesses counter & guessed letters list
MAX_WRONG_GUESSES = 6
wrong_guesses = 0
guessed_letters = []
wrong_letters=[]
print(f"You will have {MAX_WRONG_GUESSES} guesses to guess the word")



while wrong_guesses < MAX_WRONG_GUESSES:
    print(f"Incorrectly guessed letters: {wrong_letters}")
    guessed_letter = input("guess a letter here: ").lower()
    if len(guessed_letter) != 1:
        print("Your guess needs to be 1 letter long")
        continue
    if not guessed_letter.isalpha():
        print("Your guess needs to be a letter")
        continue  

    guessed_letters.append(guessed_letter)

    if guessed_letter in secret_word:
        print(f"Correct {guessed_letter} is in the word")
    else:
        print(f"Incorrect {guessed_letter} is not in the word")
        wrong_letters.append(guessed_letter)
        wrong_guesses += 1
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + f"{letter} "
        else:   
            display = display + "_ "
    
    print(display)
    