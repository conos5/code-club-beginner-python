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

import time

guess = 0
for hangman in HANGMAN_PICS:
    print(f"Guess {guess}")
    print(hangman)
    guess += 1
    time.sleep(1)

print("Game over")

print(f"The user starts at 0 guesses and has {len(HANGMAN_PICS) - 1} wrong guesses before losing")