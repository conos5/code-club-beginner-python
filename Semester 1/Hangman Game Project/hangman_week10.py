import random

print("=== HANGMAN ===\n")
print("Welcome to Hangman!")

# Game Setup

# HANGMAN ASCII ART
# Each wrong guess shows the next stage

HANGMAN_PICS = [
    # Stage 0 - No wrong guesses
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    # Stage 1 - Head
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    # Stage 2 - Body
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    # Stage 3 - Left arm
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    # Stage 4 - Right arm
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    # Stage 5 - Left leg
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    # Stage 6 - Right leg (GAME OVER)
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

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
    print(f"wrong guesses count: {wrong_guesses}")
    print(HANGMAN_PICS[wrong_guesses])
    print(f"Incorrectly guessed letters: {wrong_letters}")
    guessed_letter = input("guess a letter here: ").lower()
    if len(guessed_letter) != 1:
        print("Your guess needs to be 1 letter long")
        continue
    if not guessed_letter.isalpha():
        print("Your guess needs to be a letter")
        continue  
    if guessed_letter in guessed_letters:
        print("You have already guessed this letter")
        continue

    guessed_letters.append(guessed_letter)

    if guessed_letter in secret_word:
        print(f"Correct {guessed_letter} is in the word")
    else:
        print(f"Incorrect {guessed_letter} is not in the word")
        wrong_letters.append(guessed_letter)
        wrong_guesses += 1
    display = ""
    match_count = 0  # Win con 3
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + f"{letter} "
            match_count += 1 # Win con 3
        else:   
            display = display + "_ "

    # Add win condition here: Win con 3
    if match_count >= len(secret_word):
        print("\n" + "=" * 40)
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")
        print(f"The word was: {secret_word.upper()}")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
        print("=" * 40)
        break
    
    print(display)

# Loss condition
if wrong_guesses >= MAX_WRONG_GUESSES:
    print(HANGMAN_PICS[wrong_guesses])
    print("=" * 40)
    print("GAME OVER! You ran out of guesses!")
    print(f"The word was: {secret_word.upper()}")
    print("=" * 40)
    