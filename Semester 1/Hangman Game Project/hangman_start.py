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
print(f"You will have {MAX_WRONG_GUESSES} to guess the word")

# Now you need to make the game loop